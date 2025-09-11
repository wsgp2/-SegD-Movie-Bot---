# Этот файл отвечает за обработку inline-кнопок (callback_query).
# Сейчас реализован только один обработчик: показ деталей фильма по его id.

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

def register(bot, db):
    """
    Регистрируем обработчики callback-запросов.
    Здесь добавляем функцию, которая реагирует на call.data,
    начинающееся с 'movie:' (то есть нажатие на кнопку фильма).
    """
    bot.register_callback_query_handler(
        lambda call: _movie_details(call, bot, db),
        func=lambda call: call.data and call.data.startswith('movie:')
    )

async def _movie_details(call, bot, db):
    """
    Показывает подробности о фильме по его id.
    call.data приходит в виде 'movie:<id>'.
    """
    chat_id = call.message.chat.id
    data = call.data.split(':', 1)[1]

    # Проверяем, что id фильма корректный (число).
    try:
        movie_id = int(data)
    except:
        await bot.answer_callback_query(call.id, 'Неверный идентификатор.')
        return

    # Ищем пользователя в базе (по chat_id, который = tg_id).
    user_db = await db.get_user_by_tgid(chat_id)
    if not user_db:
        await bot.answer_callback_query(call.id, 'Сначала используйте /start.')
        return

    user_id = user_db[0]

    # Берём фильм пользователя из базы.
    movie = await db.get_movie(user_id, movie_id)
    if not movie:
        await bot.answer_callback_query(call.id, 'Фильм не найден.')
        return

    # Раскладываем данные по переменным для удобства.
    mid, title, year, rating, review, created = movie

    # Текстовое описание фильма для пользователя.
    text = f"{title} ({year})\nОценка: {rating}/10\nДобавлен: {created}\n\nОтзыв:\n{review}"

    # Отправляем сообщение с деталями фильма.
    await bot.send_message(chat_id, text)

    # Закрываем "часики" на кнопке.
    await bot.answer_callback_query(call.id)
