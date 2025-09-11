"""Точка входа бота.

Запускает и регистрирует обработчики, и запускает фоновую задачу напоминаний.
"""
import asyncio
import logging
import os

from telebot.async_telebot import AsyncTeleBot

import config
import db
import db as db_mod
from services import reminders
from handlers import messages, callbacks
from services.reminders import start_reminder_task

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = AsyncTeleBot(config.TOKEN, parse_mode='markdown')

async def main():
    # Инициализация базы
    await db_mod.init_db(config.DB_PATH)
    logger.info('DB initialized: %s', config.DB_PATH)

    # Регистрируем обработчики
    messages.register(bot, db_mod)
    callbacks.register(bot, db_mod)
    logger.info('Handlers registered')

    # Запускаем периодические задачи (напоминания)
    asyncio.create_task(start_reminder_task(bot, db, weekday=config.WEEKDAY, hour=config.HOURS, minute=config.MINUTES))

    # Запуск polling
    logger.info('Starting bot polling...')
    await bot.polling()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot stopped')
