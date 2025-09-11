"""Фоновая задача: каждую неделю в указанный день и время отправлять напоминания всем пользователям.

Простая реализация: вычисляем время до следующего указанного дня и делаем asyncio.sleep.
Для продакшна лучше использовать scheduler (APScheduler) или cron.
"""
import asyncio
from datetime import datetime, timedelta
import pytz

async def start_reminder_task(bot, db, weekday=6, hour=9, minute=0):
    """
    Запускает задачу отправки напоминаний в указанный день недели и время

    Args:
        bot: объект бота для отправки сообщений
        db: объект базы данных для получения пользователей
        weekday: день недели (0-6, где 0=понедельник, 6=воскресенье)
        hour: час отправки (0-23)
        minute: минута отправки (0-59)
    """
    tz = pytz.timezone('Europe/Moscow')
    print(datetime.now(tz))
    while True:
        now = datetime.now(tz)

        # Вычисляем следующее целевое время
        days_ahead = (weekday - now.weekday()) % 7
        if days_ahead == 0:  # Если сегодня тот же день недели
            # Проверяем, было ли уже целевое время сегодня
            target_time_today = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            if now >= target_time_today:
                # Если время уже прошло, планируем на следующую неделю
                days_ahead = 7

        # Вычисляем целевую дату и время
        target_date = now.date() + timedelta(days=days_ahead)
        target_dt = tz.localize(
            datetime.combine(target_date, datetime.min.time())
        ).replace(hour=hour, minute=minute, second=0, microsecond=0)

        wait_seconds = (target_dt - now).total_seconds()

        # Ждём до момента отправки
        await asyncio.sleep(wait_seconds)

        # Отправляем всем пользователям
        try:
            tg_ids = await db.get_all_tg_users()
            for tg_id in tg_ids:
                try:
                    # Кнопка для быстрого добавления фильма
                    from telebot.types import ReplyKeyboardMarkup, KeyboardButton
                    kb = ReplyKeyboardMarkup(resize_keyboard=True)
                    kb.add(KeyboardButton('Добавить фильм'))

                    await bot.send_message(
                        tg_id,
                        'Не забыли записать фильмы, просмотренные на неделе?',
                        reply_markup=kb
                    )
                    # Небольшая задержка между сообщениями чтобы не превысить лимиты
                    await asyncio.sleep(0.1)
                except Exception as e:
                    # Пропускаем пользователей, у которых бот заблокирован или другие ошибки
                    print(f"Ошибка отправки пользователю {tg_id}: {e}")
                    continue
        except Exception as e:
            print(f"Ошибка получения пользователей из БД: {e}")

        # После отправки ждём 1 минуту перед следующим циклом планирования
        await asyncio.sleep(60)