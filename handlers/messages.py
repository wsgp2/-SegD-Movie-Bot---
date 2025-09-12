# handlers/messages.py
# Здесь описаны обработчики текстовых сообщений и команд для бота.
# Логика:
# - команды: /start, /search, /stats, /admin, /set_admin, /unadmin
# - кнопки: добавление фильма, просмотр своих фильмов, статистика, поиск
import datetime
import os

from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Структура для хранения временных состояний пользователей в оперативной памяти.
# Ключ — chat_id пользователя, значение — словарь с полем 'action' и шагами.
user_states = {}

def _rating_keyboard():
    """
    Клавиатура с кнопками 1..10 и кнопкой 'Отмена'.
    Используется при вводе оценки фильма.
    """
    kb = ReplyKeyboardMarkup(row_width=5, resize_keyboard=True, one_time_keyboard=True)
    buttons = [KeyboardButton(str(i)) for i in range(1, 11)]
    kb.add(*buttons)
    kb.add(KeyboardButton('Отмена'))
    return kb

def _main_keyboard():
    """
    Основная клавиатура, которую видит пользователь в меню.
    """
    kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    kb.add(KeyboardButton('✍️ Добавить фильм'), KeyboardButton('🎬 Мои фильмы'))
    kb.add(KeyboardButton('🧮 Статистика'), KeyboardButton('🔎 Поиск'))
    kb.add(KeyboardButton('ℹ️ О боте'))
    return kb

def register(bot, db):
    """
    Регистрируем все обработчики команд и общий текстовый обработчик.
    Параметр db — модуль с функциями работы с базой (db.add_user, db.add_movie и т.д.).
    """
    bot.register_message_handler(lambda m: _cmd_start(m, bot, db), commands=['start'])
    bot.register_message_handler(lambda m: _cmd_search(m, bot, db), commands=['search'])
    bot.register_message_handler(lambda m: _cmd_stats(m, bot, db), commands=['stats'])
    bot.register_message_handler(lambda m: _cmd_admin(m, bot, db), commands=['admin'])
    bot.register_message_handler(lambda m: _cmd_set_admin(m, bot, db), commands=['set_admin'])
    bot.register_message_handler(lambda m: _cmd_unadmin(m, bot, db), commands=['unadmin'])
    bot.register_message_handler(lambda m: _cmd_about(m, bot, db), commands=['about'])
    # Общий обработчик всех текстовых сообщений (после команд)
    bot.register_message_handler(lambda m: _text_handler(m, bot, db), func=lambda message: True)

# -----------------------
# Команды управления админами
# -----------------------

async def _cmd_set_admin(message, bot, db):
    """
    /set_admin <tg_id>
    Добавляет номер Telegram ID в таблицу админов.
    Команду может выполнить только существующий админ.
    """
    chat_id = message.chat.id
    sender_tg = message.from_user.id

    if not await db.is_admin(sender_tg):
        await bot.send_message(chat_id, "У вас нет прав для добавления админа.")
        return

    parts = (message.text or "").strip().split()
    if len(parts) < 2:
        await bot.send_message(chat_id, "Использование: /set_admin <tg_id>")
        return
    try:
        target_tg = int(parts[1])
    except ValueError:
        await bot.send_message(chat_id, "Ошибка: <tg_id> должен быть числом (Telegram ID).")
        return

    try:
        await db.add_admin(target_tg, note=f"added by {sender_tg}")
        await bot.send_message(chat_id, f"Пользователь {target_tg} добавлен в список админов.")
    except Exception as ex:
        await bot.send_message(chat_id, f"Ошибка при добавлении админа: {ex}")

async def _cmd_unadmin(message, bot, db):
    """
    /unadmin <tg_id>
    Убирает Telegram ID из таблицы админов.
    Команду может выполнить только существующий админ.
    """
    chat_id = message.chat.id
    sender_tg = message.from_user.id

    if not await db.is_admin(sender_tg):
        await bot.send_message(chat_id, "У вас нет прав для удаления админа.")
        return

    parts = (message.text or "").strip().split()
    if len(parts) < 2:
        await bot.send_message(chat_id, "Использование: /unadmin <tg_id>")
        return
    try:
        target_tg = int(parts[1])
    except ValueError:
        await bot.send_message(chat_id, "Ошибка: <tg_id> должен быть числом (Telegram ID).")
        return

    try:
        await db.remove_admin(target_tg)
        await bot.send_message(chat_id, f"Пользователь {target_tg} удалён из списка админов (если он там был).")
    except Exception as ex:
        await bot.send_message(chat_id, f"Ошибка при удалении админа: {ex}")

# -----------------------
# Команда /admin — экспорт базы
# -----------------------

async def _cmd_admin(message, bot, db):
    """
    /admin
    Если пользователь — админ, бот формирует Excel-файл с объединёнными users+movies
    и отправляет его в чат.
    """
    chat_id = message.chat.id
    tg_id = message.from_user.id

    if not await db.is_admin(tg_id):
        await bot.send_message(chat_id, "У вас нет доступа к /admin.")
        return

    await bot.send_message(chat_id, "Генерирую экспорт базы в Excel. Подождите...")
    try:
        from config import TMP_DIR
        path = await db.export_all_to_excel(tmp_dir=TMP_DIR)
        with open(path, 'rb') as f:
            await bot.send_document(chat_id, f)
    except Exception as ex:
        await bot.send_message(chat_id, f"Ошибка при экспорте: {ex}")

# -----------------------
# Команды /start, /search, /stats
# -----------------------

async def _cmd_start(message, bot, db):
    """
    /start
    Регистрирует пользователя в базе, если его там нет, и показывает главное меню.
    """
    chat_id = message.chat.id
    # Если пользователя нет в БД — добавляем
    user_db = await db.get_user_by_tgid(chat_id)
    if not user_db:
        await db.add_user(chat_id, message.from_user.full_name)
    
    # Приветственное сообщение + клавиатура
    welcome_text = """🎬 **Добро пожаловать в Личный Кинокритик!**

Я помогу вести журнал просмотренных фильмов с рейтингами, отзывами и статистикой.

📋 **Мои возможности:**
• ✍️ Добавление фильмов с рейтингом 1-10
• 🎬 Просмотр вашей коллекции
• 🔎 Поиск по названию и отзывам
• 📊 Статистика с красивыми графиками
• 📁 Экспорт базы в Excel (для админов)

Начните с кнопки "✍️ Добавить фильм" или используйте /about для информации о создателе."""
    
    await bot.send_message(chat_id, welcome_text, reply_markup=_main_keyboard())

async def _cmd_search(message, bot, db):
    """
    /search
    Переводит пользователя в режим поиска — ожидаем ввод ключевого слова в следующем сообщении.
    """
    chat_id = message.chat.id
    user_states[chat_id] = {'action': 'searching'}
    await bot.send_message(chat_id, 'Введите ключевое слово для поиска (по названию или по тексту рецензии):')

async def _cmd_stats(message, bot, db):
    """
    /stats
    Выводит простую статистику пользователя и показывает графики просмотра.
    """
    chat_id = message.chat.id
    user_db = await db.get_user_by_tgid(chat_id)
    if not user_db:
        await bot.send_message(chat_id, 'Сначала используйте /start чтобы зарегистрироваться.')
        return

    user_id = user_db[0]
    stats = await db.get_stats(user_id)
    avg_rating = round(stats['avg'], 2) if stats['total'] > 0 else 0

    # Текст с основной статистикой
    text = f"📊 Ваша 🧮 Статистика:\n\n"
    text += f"🎬 Общее количество фильмов: {stats['total']}\n"
    text += f"⭐ Средняя оценка: {avg_rating}\n"
    if stats['top_title']:
        text += f"🏆 Лучший фильм: {stats['top_title']} — {stats['top_rating']}/10\n"

    # Генерируем графики (7, 30, 90, 365 дней)
    from services.charts import generate_charts_for_user
    chart_paths = await generate_charts_for_user(db, user_id, [7, 30, 90, 365])

    if chart_paths:
        try:
            # Читаем файлы в память и формируем список медиа для отправки
            media = []
            for i, path in enumerate(chart_paths):
                with open(path, 'rb') as f:
                    photo_data = f.read()

                # Для первой картинки добавляем подпись
                if i == 0:
                    media.append(types.InputMediaPhoto(photo_data, caption=text))
                else:
                    media.append(types.InputMediaPhoto(photo_data))

            # Отправляем все картинки одной группой
            await bot.send_media_group(chat_id, media)

        except Exception as ex:
            await bot.send_message(chat_id, f'Не удалось отправить графики: {ex}')

        # Пытаемся удалить временные файлы с графиками
        try:
            for path in chart_paths:
                if os.path.exists(path):
                    os.remove(path)
        except:
            pass
    else:
        # Если графики не сгенерировались, просто отправляем текст
        await bot.send_message(chat_id, text)

# -----------------------
# Общий текстовый обработчик
# -----------------------

async def _text_handler(message, bot, db):
    """
    Отлавливает все текстовые сообщения и:
    - обрабатывает шаги при добавлении фильма (state-machine),
    - реагирует на нажатия кнопок основного меню,
    - обрабатывает ввод для поиска.
    Даты сохраняются в ISO 8601 формате для согласования с БД.
    """
    chat_id = message.chat.id
    text = (message.text or '').strip()
    state = user_states.get(chat_id)

    # --- Работа state-machine для добавления фильма ---
    if state and state.get('action') == 'adding_movie':
        step = state.get('step')

        # Шаг: ввод названия
        if step == 'title':
            if not text or text.lower() == 'отмена':
                user_states.pop(chat_id, None)
                await bot.send_message(chat_id, 'Добавление фильма отменено.', reply_markup=_main_keyboard())
                return
            state['title'] = text
            state['step'] = 'year'
            await bot.send_message(chat_id, 'Год выхода (например, 1994):')
            return

        # Шаг: ввод года
        if step == 'year':
            if not text.isdigit():
                await bot.send_message(chat_id, 'Год должен быть числом. Введите год (например, 1994):')
                return
            state['year'] = int(text)
            state['step'] = 'rating'
            await bot.send_message(chat_id, 'Оценка (1-10):', reply_markup=_rating_keyboard())
            return

        # Шаг: ввод оценки
        if step == 'rating':
            if text.lower() == 'отмена':
                user_states.pop(chat_id, None)
                await bot.send_message(chat_id, 'Добавление фильма отменено.', reply_markup=_main_keyboard())
                return
            if not text.isdigit() or not (1 <= int(text) <= 10):
                await bot.send_message(chat_id, 'Оценка должна быть числом от 1 до 10. Пожалуйста, выберите оценку:')
                return
            state['rating'] = int(text)
            state['step'] = 'review'
            await bot.send_message(chat_id, 'Напишите ваш отзыв/рецензию (текст):')
            return

        # Шаг: ввод отзыва
        if step == 'review':
            if not text:
                await bot.send_message(chat_id, 'Отзыв не может быть пустым. Пожалуйста, напишите отзыв:')
                return
            state['review'] = text

            # --- Сохраняем фильм в базе с ISO 8601 ---
            user_db = await db.get_user_by_tgid(chat_id)
            user_id = user_db[0]
            created_iso = datetime.datetime.now().isoformat(timespec='seconds')  # формируем дату в ISO

            await db.add_movie(
                user_id,
                state['title'],
                state['year'],
                state['rating'],
                state['review'],
            )

            await bot.send_message(chat_id, f"Фильм '{state['title']}' сохранён ✅", reply_markup=_main_keyboard())
            user_states.pop(chat_id, None)
            return

    # --- Кнопка "Добавить фильм" ---
    if text == '✍️ Добавить фильм':
        user_states[chat_id] = {'action': 'adding_movie', 'step': 'title'}
        await bot.send_message(chat_id, 'Введите название фильма (обязательно):')
        return

    # --- Кнопка "Мои фильмы" ---
    if text == '🎬 Мои фильмы':
        user_db = await db.get_user_by_tgid(chat_id)
        if not user_db:
            await bot.send_message(chat_id, 'Сначала используйте /start для регистрации.')
            return
        user_id = user_db[0]
        movies = await db.get_movies(user_id)
        if not movies:
            await bot.send_message(chat_id, 'Ваш журнал пока пуст. Добавьте первый фильм — кнопка "✍️ Добавить фильм".', reply_markup=_main_keyboard())
            return

        from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
        markup = InlineKeyboardMarkup()
        for m in movies:
            mid, title, year, rating, review, created = m
            # Приводим дату к ISO, если нужно отображать
            # created_iso = datetime.fromisoformat(created).strftime('%Y-%m-%d %H:%M:%S')
            btn = InlineKeyboardButton(f"{title} ({year}) - {rating}/10", callback_data=f"movie:{mid}")
            markup.add(btn)
        await bot.send_message(chat_id, 'Ваши фильмы:', reply_markup=markup)
        return

    # --- Кнопки Статистика / Поиск / О боте ---
    if text == '🧮 Статистика':
        await _cmd_stats(message, bot, db)
        return
    elif text == '🔎 Поиск':
        await _cmd_search(message, bot, db)
        return
    elif text == 'ℹ️ О боте':
        await _cmd_about(message, bot, db)
        return

    # --- Если пользователь в режиме поиска ---
    if state and state.get('action') == 'searching':
        q = text
        user_db = await db.get_user_by_tgid(chat_id)
        if not user_db:
            await bot.send_message(chat_id, 'Сначала используйте /start для регистрации.')
            user_states.pop(chat_id, None)
            return
        user_id = user_db[0]
        rows = await db.search_movies(user_id, q)
        if not rows:
            await bot.send_message(chat_id, 'Ничего не найдено.', reply_markup=_main_keyboard())
            user_states.pop(chat_id, None)
            return

        from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
        markup = InlineKeyboardMarkup()
        for r in rows:
            mid, title, year, rating, review, created = r
            # Можно выводить дату в нужном формате:
            # display_date = datetime.fromisoformat(created).strftime('%d.%m.%Y')
            markup.add(InlineKeyboardButton(f"{title} ({year}) - {rating}/10", callback_data=f"movie:{mid}"))

        await bot.send_message(chat_id, f'Найдено {len(rows)} записей:', reply_markup=markup)
        user_states.pop(chat_id, None)
        return

# -----------------------
# Команда /about — информация о создателе
# -----------------------

async def _cmd_about(message, bot, db):
    """
    /about
    Показывает информацию о создателе бота и контакты для заказа.
    """
    chat_id = message.chat.id
    
    about_text = """О боте Личный Кинокритик

Создатель: SergD  
Telegram: https://t.me/sergei_dyshkant

Специализация:
- Telegram-боты под любые задачи
- Автоматизация бизнес-процессов  
- Интеграции с CRM, API, базами данных
- Веб-приложения и сервисы

Хотите себе бота?
Пишите помощнику: https://t.me/TomMedved

Преимущества:
- Быстрая разработка
- Качественный код
- Поддержка после запуска
- Разумные цены

Этот бот создан с использованием:
- Python + AsyncIO
- SQLite база данных  
- Matplotlib для графиков
- Развернут на Oracle Cloud

Используйте /start для возврата к меню"""
    
    await bot.send_message(chat_id, about_text)
