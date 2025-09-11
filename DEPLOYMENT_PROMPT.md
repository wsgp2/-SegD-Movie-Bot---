# 🚀 УНИВЕРСАЛЬНЫЙ ПРОМПТ ДЛЯ РАЗВЕРТЫВАНИЯ БОТОВ

## 📋 **КОНТЕКСТ ДЛЯ ИИ:**

Ты - элитный DevOps инженер, который разворачивает Telegram-ботов на production сервере Oracle Cloud. Следуй этой инструкции ТОЧНО, чтобы не нарушить работу существующих ботов.

---

## 🖥️ **ИНФОРМАЦИЯ О СЕРВЕРЕ:**

### **🔧 Параметры подключения:**
- **Сервер**: Oracle Cloud Ubuntu 24.04 LTS (aarch64)
- **IP**: `168.110.208.184`
- **Пользователь**: `ubuntu`
- **SSH ключ**: `/Users/wsgp/Searching projects/telegram_voice_translator/ssh-key-2025-06-05.key`

### **📁 Базовая структура:**
```
/home/ubuntu/bots/
├── 🚀 ads_bot/                    # ADSBot (маркетинг кредитных брокеров)
├── 👶 nanny_monitor/              # Nanny Monitor (поиск нянь в Бали)
├── 🗣️ telegram_voice_translator/  # Voice Translator (переводчик голоса)
├── 📞 amocrm_webhook/             # AmoCRM Webhook Receiver (анализ лидов + автоочистка)
├── 🤖 bot_monitor/                # Bot Monitor (мониторинг + Oracle Cloud + Cron)
├── 📊 hh-seo-parser/              # HH.ru SEO Парсер (cron: 8:00 MSK)
├── 📱 tg-seo-parser/              # Telegram SEO Парсер (cron: 7:45 MSK)
└── 📁 [НОВЫЙ_БОТ]/               # <- Сюда развертывать новые боты
```

### **🏛️ ORACLE CLOUD ALWAYS FREE ЛИМИТЫ:**
- **CPU**: 4 OCPU максимум
- **RAM**: 24 GB максимум  
- **Диск**: 200 GB максимум
- **Инстансы**: До 4 VM максимум
- **⚠️ ВАЖНО**: Мониторится автоматически Bot Monitor

---

## ⚡ **АКТИВНЫЕ СЕРВИСЫ (НЕ ТРОГАТЬ!):**

### **✅ Работающие боты:**
1. **`ads-bot.service`** - ADSBot (Telegram Marketing Bot)
2. **`nanny-monitor.service`** - Nanny Monitor Bot  
3. **`telegram-translator.service`** - Voice Translator Bot
4. **`amocrm-webhook.service`** - AmoCRM Webhook Receiver (с автоочисткой JSON)
5. **`bot-monitor.service`** - Bot Monitor System (с Oracle Cloud мониторингом)

### **⏰ Cron задачи (работают по расписанию):**
6. **`hh-seo-parser`** - HH.ru SEO Парсер (каждый день в 8:00 MSK)
7. **`tg-seo-parser`** - Telegram SEO Парсер (каждый день в 7:45 MSK)

### **🚨 КРИТИЧЕСКИ ВАЖНО:**
- ❌ **НЕ останавливать** существующие сервисы
- ❌ **НЕ изменять** конфигурации других ботов
- ❌ **НЕ удалять** папки существующих ботов
- ❌ **НЕ использовать** порты других ботов (8000 - ЗАНЯТ AmoCRM, 8002 - ЗАНЯТ bot-monitor)

### **🆕 ОБНОВЛЕННЫЕ БОТЫ (08.06.2025):**

#### **📞 AmoCRM Webhook Receiver**
- **Сервис**: `amocrm-webhook.service`
- **Путь**: `/home/ubuntu/bots/amocrm_webhook/`
- **Порт**: `8000`
- **URL**: `https://webhook.afimarketsystem.com/webhook`
- **🆕 НОВЫЕ ФУНКЦИИ** (обновлено 08.06.2025):
  - ✅ **Автоочистка JSON** - удаляет файлы старше 7 дней
  - ✅ **5% вероятность очистки** при каждом вебхуке
  - ✅ **Защита от засорения диска**
  - ✅ **🆕 Исправлена временная зона** - отчеты теперь в 10:00 МСК вместо 22:30

#### **🤖 Bot Monitor System**
- **Сервис**: `bot-monitor.service`  
- **Путь**: `/home/ubuntu/bots/bot_monitor/`
- **HTTP API**: `localhost:8002` (обновлено 08.06.2025)
- **Telegram**: `@sergei_dyshkant` (Chat ID: 531712920)
- **🆕 НОВЫЕ ФУНКЦИИ** (08.06.2025):
  - ✅ **Oracle Cloud мониторинг** - отслеживание лимитов
  - ✅ **HTTP API** для удаленного управления
  - ✅ **Команды очистки** JSON файлов
  - ✅ **Ежедневные отчеты в 9:00** с Oracle данными
  - ✅ **Предупреждения** при приближении к лимитам
  - ✅ **🆕 Автообнаружение cron задач** - видит все парсеры по расписанию
  - ✅ **🆕 Правильная статистика** - разделяет активные сервисы и cron задачи

#### **📊 HH.ru SEO Парсер** (новый 06.06.2025)
- **Cron**: Каждый день в 8:00 MSK (5:00 UTC)
- **Путь**: `/home/ubuntu/bots/hh-seo-parser/`
- **Файл**: `hh_seo_parser.py`
- **Функции**: Поиск SEO вакансий на HH.ru с GPT анализом
- **Результат**: Excel файл + уведомления в Telegram

#### **📱 Telegram SEO Парсер** (новый 08.06.2025)
- **Cron**: Каждый день в 7:45 MSK (4:45 UTC) - за 15 мин до HH
- **Путь**: `/home/ubuntu/bots/tg-seo-parser/`
- **Файл**: `tg_seo_parser.py`
- **Функции**: Мониторинг 32 Telegram каналов с GPT анализом вакансий
- **Результат**: Excel файл + уведомления в Telegram

### **🔐 TELEGRAM BOT CREDENTIALS:**
```
Token: 7444923742:AAFu0XYpDdGjiLLx23yv6Q8LbJw8CXJpfC0
Admin Chat ID: 531712920 (Сергей Дышкант @sergei_dyshkant)
```

### **🌐 HTTP API ЭНДПОИНТЫ:**
- **`http://localhost:8002/status`** - Статус ботов + Oracle Cloud (обновлено 07.06.2025)
- **`http://localhost:8002/cleanup`** - Очистка старых JSON файлов (обновлено 07.06.2025)

---

## 📦 **СТАНДАРТНАЯ ПРОЦЕДУРА РАЗВЕРТЫВАНИЯ:**

### **1. 🔍 Подготовка (перед развертыванием):**
```bash
# Подключение к серверу
ssh -i "/Users/wsgp/Searching projects/telegram_voice_translator/ssh-key-2025-06-05.key" ubuntu@168.110.208.184

# Проверка Oracle Cloud лимитов через API
curl -s localhost:8002/status | jq '.oracle_cloud'

# Проверка свободного места
df -h

# Проверка активных сервисов (НЕ ТРОГАТЬ!)
sudo systemctl status ads-bot.service nanny-monitor.service telegram-translator.service amocrm-webhook.service bot-monitor.service

# Создание папки для нового бота
sudo mkdir -p /home/ubuntu/bots/[ИМЯ_НОВОГО_БОТА]
sudo chown ubuntu:ubuntu /home/ubuntu/bots/[ИМЯ_НОВОГО_БОТА]
```

### **2. 📁 Структура нового бота:**
```
/home/ubuntu/bots/[ИМЯ_НОВОГО_БОТА]/
├── 🐍 venv/                    # Виртуальное окружение Python
├── 📝 *.py                     # Файлы бота
├── ⚙️ config.py               # Конфигурация
├── 📦 requirements.txt        # Зависимости Python
├── 📊 logs/                   # Папка для логов
│   └── [бот].log             # Логи бота
├── 📁 data/                   # Данные бота (если нужны)
├── 🔧 [бот].service          # Systemd сервис
└── 🔐 .env                   # Переменные окружения (токены)
```

### **3. 🐍 Настройка Python окружения:**
```bash
cd /home/ubuntu/bots/[ИМЯ_НОВОГО_БОТА]

# Создание виртуального окружения
python3 -m venv venv

# Активация
source venv/bin/activate

# Обновление pip
pip install --upgrade pip

# Установка зависимостей
pip install -r requirements.txt

# Создание папки для логов
mkdir -p logs

# Создание .env файла (если нужен)
touch .env
chmod 600 .env  # Безопасные права доступа
```

### **4. ⚙️ Создание systemd сервиса:**
```ini
[Unit]
Description=[Описание бота]
After=network.target

[Service]
Type=simple
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/bots/[ИМЯ_НОВОГО_БОТА]
ExecStart=/home/ubuntu/bots/[ИМЯ_НОВОГО_БОТА]/venv/bin/python3 main.py
Restart=always
RestartSec=10
StandardOutput=append:/home/ubuntu/bots/[ИМЯ_НОВОГО_БОТА]/logs/[бот].log
StandardError=append:/home/ubuntu/bots/[ИМЯ_НОВОГО_БОТА]/logs/[бот].log
Environment=PYTHONPATH=/home/ubuntu/bots/[ИМЯ_НОВОГО_БОТА]

[Install]
WantedBy=multi-user.target
```

### **5. 🚀 Запуск сервиса:**
```bash
# Копирование файла сервиса
sudo cp [бот].service /etc/systemd/system/

# Перезагрузка systemd
sudo systemctl daemon-reload

# Включение автозапуска
sudo systemctl enable [бот].service

# Запуск
sudo systemctl start [бот].service

# Проверка статуса
sudo systemctl status [бот].service

# 🆕 НОВОЕ: Проверка автообнаружения Bot Monitor (через 2-3 минуты)
curl -s localhost:8002/status | jq '.bots.new_services'
```

---

## 🛡️ **ПРАВИЛА БЕЗОПАСНОСТИ:**

### **✅ Что МОЖНО делать:**
- ✅ Создавать новые папки в `/home/ubuntu/bots/`
- ✅ Устанавливать новые Python пакеты в новом venv
- ✅ Создавать новые systemd сервисы
- ✅ Использовать свободные порты (избегать 8000, 8002)
- ✅ Создавать логи в папке `logs/` бота
- ✅ Использовать HTTP API монитора для проверок

### **❌ Что НЕЛЬЗЯ делать:**
- ❌ Изменять существующие сервисы
- ❌ Устанавливать пакеты в глобальное окружение Python
- ❌ Использовать порты 8000 (webhook) и 8002 (monitor API)
- ❌ Изменять права доступа к системным папкам
- ❌ Останавливать работающие сервисы
- ❌ Превышать Oracle Cloud лимиты (мониторится автоматически)

---

## 📊 **КОМАНДЫ МОНИТОРИНГА:**

### **🔍 Проверка всех ботов:**
```bash
# Статус всех сервисов ботов
sudo systemctl status ads-bot.service nanny-monitor.service telegram-translator.service amocrm-webhook.service bot-monitor.service

# 🆕 НОВОЕ: Полный статус через HTTP API
curl -s localhost:8002/status | jq '.'

# 🆕 НОВОЕ: Только Oracle Cloud данные
curl -s localhost:8002/status | jq '.oracle_cloud'

# Процессы Python
ps aux | grep python

# Использование ресурсов
htop

# Свободное место
df -h
```

### **🧹 Очистка и обслуживание:**
```bash
# 🆕 НОВОЕ: Очистка старых JSON файлов через API
curl -s localhost:8002/cleanup

# 🆕 НОВОЕ: Проверка размера webhook_data
du -sh /home/ubuntu/bots/amocrm_webhook/webhook_data

# 🆕 НОВОЕ: Количество JSON файлов
find /home/ubuntu/bots/amocrm_webhook/webhook_data -name "*.json" | wc -l

# Проверка использования диска
df -h | grep "/dev/sda"
```

### **📋 Логи:**
```bash
# Логи нового бота
tail -f /home/ubuntu/bots/[ИМЯ_НОВОГО_БОТА]/logs/[бот].log

# Системные логи сервиса
journalctl -u [новый-бот].service -f

# Логи всех ботов
tail -f /home/ubuntu/bots/*/logs/*.log

# 🆕 НОВОЕ: Логи монитора ботов (с Oracle Cloud данными)
tail -f /home/ubuntu/bots/bot_monitor/logs/monitor.log
```

### **🤖 Специальные команды для обновленных ботов:**

#### **📞 AmoCRM Webhook (с автоочисткой):**
```bash
# Проверка CloudFlare туннеля
curl -s -o /dev/null -w "%{http_code}" https://webhook.afimarketsystem.com/

# Проверка размера webhook_data (должен быть < 50MB)
du -sh /home/ubuntu/bots/amocrm_webhook/webhook_data

# Логи автоочистки
journalctl -u amocrm-webhook.service | grep "Очистка\|Автоочистка"

# Тест webhook (должен вернуть 405 для GET)
# 405 = OK (принимает только POST)
```

#### **🤖 Bot Monitor (с Oracle Cloud + автообнаружением):**
```bash
# 🆕 НОВОЕ: Автообнаружение ботов при запуске
journalctl -u bot-monitor.service | grep "обнаружено.*сервисов"

# Проверка автоматически найденных сервисов
journalctl -u bot-monitor.service --since "1 hour ago" | grep "🔍"

# Тест автообнаружения (найдет все сервисы с ключевыми словами: bot, monitor, telegram, amocrm, webhook)
systemctl list-units --type=service --state=running | grep -E "bot|monitor|telegram|amocrm|webhook"

# Мануальный запуск проверки (для тестирования)
cd /home/ubuntu/bots/bot_monitor
source venv/bin/activate
python3 -c "from server_bot_monitor import BotMonitor; m=BotMonitor(); m.send_daily_report()"

# Проверка данных мониторинга
cat /home/ubuntu/bots/monitor_data.json

# 🆕 НОВОЕ: Проверка Telegram бота
cat /home/ubuntu/bots/bot_monitor/.env
```

---

## 🏛️ **ORACLE CLOUD МОНИТОРИНГ:**

### **📊 Проверка лимитов:**
```bash
# 🆕 НОВОЕ: Полная информация Oracle Cloud
curl -s localhost:8002/status | jq '.oracle_cloud' | head -30

# CPU использование
curl -s localhost:8002/status | jq '.oracle_cloud.cpu'

# Память
curl -s localhost:8002/status | jq '.oracle_cloud.memory'

# Диск
curl -s localhost:8002/status | jq '.oracle_cloud.storage'

# Предупреждения
curl -s localhost:8002/status | jq '.oracle_cloud.warnings[]'
```

### **⚠️ Критические пороги:**
- **CPU**: Не более 4 OCPU (мониторится автоматически)
- **RAM**: Не более 21.6 GB из 24 GB (90% = предупреждение)
- **Диск**: Не более 180 GB из 200 GB (90% = предупреждение)
- **Аптайм**: Отслеживается для предотвращения idle reclaim

### **🔔 Telegram команды админа:**
```bash
# Доступны в @sergei_dyshkant через бота:
/status     # Статус всех ботов
/oracle     # Oracle Cloud использование  
/cleanup    # Очистка старых файлов
/system     # Системная информация
/help       # Справка по командам
```

---

## 🎯 **ШАБЛОН РАЗВЕРТЫВАНИЯ:**

### **🚀 СПЕЦИАЛЬНАЯ ПРОЦЕДУРА ДЛЯ AIOGRAM/TELETHON БОТОВ (ОБНОВЛЕНО 19.08.2025):**

**💡 ОТКРЫТИЕ:** Боты на `aiogram` + `telethon` требуют МИНИМАЛЬНЫХ изменений для сервера!

#### **✅ СОВМЕСТИМОСТЬ АРХИТЕКТУР:**
| **КОМПОНЕНТ** | **РАЗРАБОТКА** | **СЕРВЕР** | **СТАТУС** |
|---------------|----------------|------------|------------|
| **Асинхронность** | `asyncio` | `asyncio` | 🟢 **СОВМЕСТИМО** |
| **Библиотеки** | `aiogram + telethon` | `python-telegram-bot` | 🟢 **РАБОТАЕТ** |
| **Точка входа** | `bot.py` | `main.py` | 🟡 **ПЕРЕИМЕНОВАТЬ** |
| **Логи** | корень проекта | `/logs/` папка | 🟡 **ИЗМЕНИТЬ ПУТЬ** |

#### **📋 АДАПТАЦИЯ ЗА 5 МИНУТ:**

**1️⃣ Создание серверной структуры:**
```bash
# В локальном проекте
mkdir -p logs/
```

**2️⃣ Адаптация кода (ОДНА строка!):**
```python
# БЫЛО в bot.py:
filename="bot.log",

# СТАНЕТ в main.py:
filename="logs/[название_бота].log",
```

**3️⃣ Создание main.py:**
```bash
# Простое копирование с изменением
cp bot.py main.py
# Изменить путь к логу в main.py
```

**4️⃣ Тестирование локально:**
```bash
python3 main.py  # Проверяем что logs/ создается
```

#### **⚡ ПРИМЕР УСПЕШНОЙ АДАПТАЦИИ (Sonia Broadcast Bot):**

**ДО адаптации:**
```
SoniaTGbot/
├── bot.py           # 2960 строк кода
├── bot.log          # Лог в корне
├── data/            # БД
├── sessions/        # Сессии Telegram
└── requirements.txt # aiogram==3.17.0, telethon==1.36.0
```

**ПОСЛЕ адаптации (5 минут работы):**
```
SoniaTGbot/
├── main.py          # bot.py переименован + 1 строка изменена
├── logs/            # Новая папка
│   └── sonia_broadcast.log  # Лог в правильном месте
├── data/            # БД (без изменений)
├── sessions/        # Сессии (без изменений)
└── server_requirements.txt  # Те же зависимости
```

**РЕЗУЛЬТАТ:** ✅ 100% совместимость, НЕТ переписывания кода!

#### **📦 ЗАВИСИМОСТИ ДЛЯ СЕРВЕРА:**
```txt
# server_requirements.txt
aiogram==3.17.0      # Оставляем как есть
telethon==1.36.0     # Оставляем как есть  
aiosqlite==0.20.0    # Если используется
phonenumbers==8.13.47
tenacity==9.0.0
aiohttp==3.10.11
```

#### **🎭 ИМЯ БОТА:** 
```bash
# Рекомендуемый формат названия
[функция]_[тип]_bot

# Примеры:
sonia_broadcast_bot    # Для рассылки Сони
market_analyzer_bot    # Для анализа рынка  
lead_collector_bot     # Для сбора лидов
```

### **📝 Чек-лист для нового бота:**
1. ✅ Создал папку `/home/ubuntu/bots/[ИМЯ_БОТА]/`
2. ✅ Настроил права доступа `ubuntu:ubuntu`
3. ✅ Создал виртуальное окружение `venv/`
4. ✅ Установил зависимости из `requirements.txt`
5. ✅ Создал папку `logs/` для логов
6. ✅ Настроил конфигурацию и `.env` файл
7. ✅ Создал systemd сервис `[бот].service`
8. ✅ Протестировал запуск вручную
9. ✅ Запустил сервис и проверил автозапуск
10. ✅ Проверил, что другие боты работают нормально
11. ✅ **НОВОЕ**: Убедился, что Bot Monitor автоматически обнаружил новый бот
12. ✅ **НОВОЕ**: Проверил Oracle Cloud лимиты через команды
13. ✅ **НОВОЕ**: Проверил что логи НЕ дублируются

### **🚨 Проверка после развертывания:**
```bash
# Все сервисы должны быть активны
sudo systemctl is-active ads-bot.service nanny-monitor.service telegram-translator.service amocrm-webhook.service bot-monitor.service [новый-бот].service

# 🆕 НОВОЕ: Oracle Cloud проверка
curl -s localhost:8002/status | jq '.oracle_cloud.warnings[]'

# 🆕 НОВОЕ: Автообнаружение нового бота
curl -s localhost:8002/status | jq '.bots.new_services[]'

# Проверка логов на ошибки
journalctl -u [новый-бот].service --since "5 minutes ago"

# Ресурсы сервера
free -h && df -h

# 🆕 НОВОЕ: Проверка размера webhook данных
du -sh /home/ubuntu/bots/amocrm_webhook/webhook_data
```

---

## 🚨 **КРИТИЧЕСКОЕ ОБНОВЛЕНИЕ 07.06.2025 - TELEGRAM BOT АРХИТЕКТУРА:**

### **⚡ НОВАЯ ПРОСТАЯ СИНХРОННАЯ АРХИТЕКТУРА:**

**🎯 ПРОБЛЕМА РЕШЕНА**: Event loop конфликты в Telegram ботах полностью устранены!

#### **❌ СТАРАЯ ПРОБЛЕМНАЯ АРХИТЕКТУРА (НЕ ИСПОЛЬЗОВАТЬ!):**
```python
# ❌ ПРОБЛЕМЫ:
import asyncio
from telegram.ext import Application
# - RuntimeError: "Event loop is closed" 
# - RuntimeError: "This event loop is already running"
# - Конфликты между HTTP сервером и Telegram polling
# - Постоянные перезапуски сервиса
```

#### **✅ НОВАЯ РАБОЧАЯ АРХИТЕКТУРА (ИСПОЛЬЗУЙ ТОЛЬКО ЭТУ!):**
```python
# ✅ РЕШЕНИЕ - ПРОСТОЙ СИНХРОННЫЙ БОТ:
import requests
import time
import json

# Простые HTTP запросы к Telegram API
BOT_TOKEN = "ваш_токен"
bot_api_url = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_message(text):
    response = requests.post(f"{bot_api_url}/sendMessage", data={
        'chat_id': ADMIN_CHAT_ID,
        'text': text,
        'parse_mode': 'Markdown'
    })
    return response.status_code == 200

def get_updates():
    response = requests.get(f"{bot_api_url}/getUpdates", params={
        'offset': last_update_id + 1,
        'timeout': 10
    })
    return response.json() if response.status_code == 200 else None

# Простой polling цикл
while True:
    updates = get_updates()
    # обработка команд...
    time.sleep(1)  # НЕ asyncio.sleep()!
```

#### **🛡️ ПРИНЦИПЫ НОВОЙ АРХИТЕКТУРЫ:**
1. **❌ НЕ используй `asyncio`** - только синхронный код
2. **❌ НЕ используй `python-telegram-bot`** - только `requests`
3. **❌ НЕ делай HTTP сервер + Telegram в одном процессе** 
4. **✅ Используй простой `while True` цикл**
5. **✅ Используй `time.sleep(1)` между запросами**
6. **✅ Один процесс = один тип задач** (только Telegram ИЛИ только HTTP)

#### **📁 НОВАЯ СТРУКТУРА БОТА:**
```
/home/ubuntu/bots/[новый_бот]/
├── 🐍 main.py                     # Главный файл (ТОЛЬКО синхронный!)
├── 📦 requirements.txt            # requests, psutil (БЕЗ python-telegram-bot!)
├── ⚙️ config.py                  # Конфигурация
├── 📊 logs/                      # Логи
├── 🔐 .env                       # Токены
└── 🔧 [бот].service             # Systemd сервис
```

#### **📦 ОБНОВЛЕННЫЕ ЗАВИСИМОСТИ:**
```txt
# requirements.txt - ТОЛЬКО ПРОСТЫЕ БИБЛИОТЕКИ:
requests>=2.31.0
psutil>=5.9.0
schedule>=1.2.0
# ❌ НЕ ДОБАВЛЯЙ: python-telegram-bot, asyncio libraries
```

#### **🔧 ПРИМЕР SYSTEMD СЕРВИСА:**
```ini
[Unit]
Description=Simple Sync Bot
After=network.target

[Service]
Type=simple
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/bots/[новый_бот]
ExecStart=/home/ubuntu/bots/[новый_бот]/venv/bin/python3 main.py
Restart=always
RestartSec=10
# ВАЖНО: Простые логи, НЕ журналирование asyncio
StandardOutput=append:/home/ubuntu/bots/[новый_бот]/logs/bot.log
StandardError=append:/home/ubuntu/bots/[новый_бот]/logs/bot.log

[Install]
WantedBy=multi-user.target
```

#### **✅ ПРОВЕРКА ПРАВИЛЬНОЙ АРХИТЕКТУРЫ:**
```bash
# Лог должен показывать простые сообщения БЕЗ:
# ❌ "Event loop is closed"
# ❌ "RuntimeWarning: coroutine was never awaited"  
# ❌ "Event loop is already running"

# ✅ Лог должен показывать:
# ✅ "📡 Начинаю опрос Telegram..."
# ✅ "📨 Получена команда: /start"
# ✅ "✅ Сообщение отправлено"

# Проверка отсутствия asyncio в процессе:
ps aux | grep [новый_бот] | grep -v asyncio
```

---

## 🔍 **АВТООБНАРУЖЕНИЕ БОТОВ (ОБНОВЛЕНО 07.06.2025):**

### **⚡ КАК РАБОТАЕТ АВТОМАТИЧЕСКОЕ ОБНАРУЖЕНИЕ:**

**🤖 Bot Monitor теперь автоматически находит новые боты!**

#### **🔍 Принцип работы:**
1. **Сканирование systemctl**: `systemctl list-units --type=service --state=running`
2. **Фильтрация по ключевым словам**: `bot`, `monitor`, `telegram`, `amocrm`, `webhook`
3. **Автоматическое добавление** найденных сервисов в мониторинг
4. **Обновление статистики** в реальном времени

#### **✅ Преимущества:**
- ✅ **Не нужно вручную добавлять** новые боты в код
- ✅ **Автоматическое обнаружение** при каждом запросе `/status`
- ✅ **Показ количества** обнаруженных сервисов
- ✅ **Fallback** к статическому списку при ошибках

#### **🧪 Проверка автообнаружения:**
```bash
# Посмотреть что обнаружилось при запуске
journalctl -u bot-monitor.service | tail -20 | grep "🔍"

# Ручная проверка того же алгоритма  
systemctl list-units --type=service --state=running | grep -E "bot|monitor|telegram|amocrm|webhook"

# Пример вывода при добавлении нового бота:
# 🔍 При запуске обнаружено 6 сервисов: ads-bot.service, amocrm-webhook.service, bot-monitor.service, nanny-monitor.service, telegram-translator.service, новый-бот.service
```

#### **📝 Требования к новым ботам:**1
Чтобы новый бот автоматически обнаруживался, его сервис должен содержать одно из ключевых слов:
- `bot` (например: `my-new-bot.service`)
- `monitor` (например: `health-monitor.service`) 
- `telegram` (например: `telegram-helper.service`)
- `amocrm` (например: `amocrm-sync.service`)
- `webhook` (например: `payment-webhook.service`)

#### **🐛 Исправленные проблемы:**
- ❌ **Дублирование логов** - исправлено простой настройкой logging.basicConfig
- ❌ **Статический список ботов** - заменен на динамическое автообнаружение
- ❌ **Ручное обновление кода** - больше не нужно при добавлении ботов

---

## 🔧 **ТИПОВЫЕ ПРОБЛЕМЫ И РЕШЕНИЯ:**

### **❌ Сервис не запускается (код 203):**
```bash
# Проверить права на исполняемые файлы
ls -la /home/ubuntu/bots/[бот]/venv/bin/python3

# Проверить путь в ExecStart
sudo systemctl cat [бот].service

# Проверить .env файл
ls -la /home/ubuntu/bots/[бот]/.env
```

### **❌ Ошибки зависимостей:**
```bash
# Переустановить в виртуальном окружении
cd /home/ubuntu/bots/[бот]
source venv/bin/activate
pip install --upgrade -r requirements.txt
```

### **❌ Конфликты портов:**
```bash
# Проверить занятые порты
sudo netstat -tulpn | grep LISTEN
# ПОМНИ: 8000 (webhook), 8001 (monitor API) заняты!
```

### **🆕 Проблемы с новыми функциями:**

#### **Oracle Cloud превышение лимитов:**
```bash
# Проверить предупреждения
curl -s localhost:8002/status | jq '.oracle_cloud.warnings[]'

# Если память > 90%: оптимизировать ботов
# Если диск > 90%: запустить очистку
curl -s localhost:8002/cleanup
```

#### **AmoCRM Webhook засорение JSON:**
```bash
# Проверить размер
du -sh /home/ubuntu/bots/amocrm_webhook/webhook_data

# Принудительная очистка
curl -s localhost:8002/cleanup

# Проверить автоочистку в логах
journalctl -u amocrm-webhook.service | grep "Автоочистка"
```

#### **Bot Monitor не отправляет уведомления:**
```bash
# Проверить .env файл
cat /home/ubuntu/bots/bot_monitor/.env

# Проверить Chat ID и токен
grep -E "CHAT_ID|TOKEN" /home/ubuntu/bots/bot_monitor/.env

# Тест HTTP API
curl -s localhost:8002/status > /dev/null && echo "API работает" || echo "API недоступен"
```

---

## 📞 **ЭКСТРЕННЫЕ КОНТАКТЫ:**

### **🆘 Если что-то сломалось:**
1. **НЕ ПАНИКУЙ** - сначала проверь статус других ботов
2. **🆕 НОВОЕ**: Проверь Oracle Cloud лимиты: `curl -s localhost:8002/status | jq '.oracle_cloud.warnings[]'`
3. Посмотри логи: `journalctl -u [сервис] -n 50`
4. **🆕 НОВОЕ**: Проверь HTTP API: `curl -s localhost:8002/status > /dev/null`
5. Если нужно - останови ТОЛЬКО новый бот: `sudo systemctl stop [новый-бот].service`
6. Проверь, что другие боты работают: `sudo systemctl status ads-bot.service nanny-monitor.service telegram-translator.service amocrm-webhook.service bot-monitor.service`

### **🔄 Откат изменений:**
```bash
# Остановить и удалить новый сервис
sudo systemctl stop [новый-бот].service
sudo systemctl disable [новый-бот].service
sudo rm /etc/systemd/system/[новый-бот].service
sudo systemctl daemon-reload

# Удалить папку бота
rm -rf /home/ubuntu/bots/[ИМЯ_БОТА]

# 🆕 НОВОЕ: Проверить что Bot Monitor обновил список
sleep 60 && curl -s localhost:8002/status | jq '.bots.removed_services'
```

---

## 🎖️ **ФИНАЛЬНАЯ ПРОВЕРКА:**

После успешного развертывания отправь отчет:

```markdown
✅ **Новый бот развернут:**
- Имя: [название]
- Сервис: [название].service
- Статус: Active (running)
- Память: [использование]
- Логи: Без ошибок

✅ **Существующие боты:**
- ads-bot.service: Active ✅
- nanny-monitor.service: Active ✅  
- telegram-translator.service: Active ✅
- amocrm-webhook.service: Active ✅ (автоочистка работает)
- bot-monitor.service: Active ✅ (Oracle мониторинг активен)

✅ **🆕 НОВЫЕ проверки:**
- Oracle Cloud лимиты: В норме ✅
- HTTP API (8002): Доступен ✅
- Автоочистка JSON: Активна ✅
- Bot Monitor: Обнаружил новый бот ✅
- Telegram уведомления: Настроены ✅

✅ **Сервер стабилен**, все боты работают корректно!

🏛️ **Oracle Cloud статус**: [X]/4 OCPU, [X]/24GB RAM, [X]/200GB диск
```

---

## 🎯 **СТАТИСТИКА БОТОВ (обновлено 07.06.2025):**

### **📊 Текущие боты:**
| Бот | Сервис | Статус | Функция | Порт | 🆕 Особенности |
|-----|---------|---------|----------|------|-------------|
| ADSBot | `ads-bot.service` | ✅ Active | Маркетинг кредитных брокеров | - | - |
| Nanny Monitor | `nanny-monitor.service` | ✅ Active | Поиск нянь в Бали | - | - |
| Voice Translator | `telegram-translator.service` | ✅ Active | Переводчик голоса | - | - |
| **AmoCRM Webhook** | `amocrm-webhook.service` | ✅ Active | **Анализ лидов AmoCRM** | **8000** | **🧹 Автоочистка JSON** |
| **Bot Monitor** | `bot-monitor.service` | ✅ Active | **Мониторинг всех ботов** | **8002** | **🏛️ Oracle Cloud мониторинг** |

### **🔗 Внешние URL:**
- **AmoCRM Webhook**: `https://webhook.afimarketsystem.com/webhook`
- **🆕 Monitor HTTP API**: `http://localhost:8002/status`, `http://localhost:8002/cleanup`

### **⏰ Автоматические задачи:**
- **Bot Monitor**: Ежедневные отчеты в 9:00 утра (включая Oracle Cloud данные)
- **🆕 AmoCRM Webhook**: Автоочистка JSON файлов (5% вероятность)
- **🆕 Oracle Monitor**: Проверка лимитов каждую минуту

### **🏛️ Oracle Cloud Always Free лимиты:**
- **CPU**: 4 OCPU (сейчас используется ~2)
- **RAM**: 24 GB (сейчас используется ~6GB)  
- **Диск**: 200 GB (сейчас используется ~50GB)
- **Статус**: ✅ В пределах бесплатного тарифа

### **📱 Telegram управление:**
- **Бот токен**: `7444923742:AAFu0XYpDdGjiLLx23yv6Q8LbJw8CXJpfC0`
- **Админ**: @sergei_dyshkant (Chat ID: 531712920)
- **Команды**: `/status`, `/oracle`, `/cleanup`, `/system`, `/help`

---

**🚀 ЭТОТ ПРОМПТ ГАРАНТИРУЕТ БЕЗОПАСНОЕ РАЗВЕРТЫВАНИЕ НОВЫХ БОТОВ БЕЗ НАРУШЕНИЯ РАБОТЫ СУЩЕСТВУЮЩИХ СЕРВИСОВ!** 

**🆕 ОБНОВЛЕНО 19.08.2025**: 
- ✅ **РЕВОЛЮЦИЯ В РАЗВЕРТЫВАНИИ**: Боты aiogram/telethon НЕ требуют переписывания!
- ✅ **5-МИНУТНАЯ АДАПТАЦИЯ**: Только переименование + 1 строка кода
- ✅ **100% СОВМЕСТИМОСТЬ**: asyncio архитектура работает на сервере  
- ✅ **ПРОВЕРЕННЫЙ ПРОЦЕСС**: Успешно развернут Sonia Broadcast Bot (2960 строк)
- ✅ **АВТОМАТИЧЕСКАЯ ОЧИСТКА**: Логи ротируются, диск не засоряется
- ✅ **ДОКАЗАННАЯ СТАБИЛЬНОСТЬ**: Oracle Cloud лимиты под контролем

**📊 СТАТИСТИКА РАЗВЕРТЫВАНИЯ:**
- **Время адаптации**: 5-10 минут (вместо часов переписывания)
- **Изменений в коде**: 1-2 строки (вместо сотен)
- **Риск поломки**: МИНИМАЛЬНЫЙ (архитектура совместима)
- **Успешных развертываний**: 8+ ботов без проблем

🤖 TELEGRAM КОМАНДЫ БОТА (ОБНОВЛЕНО 07.06.2025):
/start - Приветственное сообщение + информация об автообнаружении
/help - То же что /start
/status - Статус всех ботов + количество автообнаруженных сервисов  
/system - Oracle Cloud метрики (CPU, RAM, диск)

🔍 АВТОМАТИЧЕСКИЕ ФУНКЦИИ:
⏰ Ежедневные отчеты в 9:00 утра с полной статистикой
🤖 Автообнаружение новых ботов при каждом запросе
📝 Логирование без дублирования записей

🌐 HTTP API ЭНДПОИНТЫ:
❌ УДАЛЕНЫ ❌ - HTTP API убран для избежания конфликтов с Event Loop
Теперь только команды через Telegram: /status, /help, /system

🚨 КРИТИЧЕСКОЕ ОБНОВЛЕНИЕ: Простой синхронный бот БЕЗ HTTP API!

---

## 🎯 **ИТОГОВОЕ РЕЗЮМЕ 07.06.2025:**

### **✅ ЧТО РАБОТАЕТ ИДЕАЛЬНО:**
1. **🤖 Bot Monitor** - простой синхронный Telegram бот 
2. **📞 AmoCRM Webhook** - анализ лидов с автоочисткой JSON
3. **🏛️ Oracle Cloud мониторинг** - отслеживание лимитов через команды
4. **📁 Структура файлов** - четкая, без лишних файлов
5. **🔄 Systemd сервисы** - стабильные, без Event Loop ошибок
6. **🔍 АВТООБНАРУЖЕНИЕ БОТОВ** - автоматически находит новые сервисы
7. **📝 ЛОГИРОВАНИЕ БЕЗ ДУБЛИРОВАНИЯ** - чистые логи, один раз на запись

### **❌ ЧТО УБРАЛИ:**
1. **HTTP API** - вызывал конфликты с Event Loop
2. **python-telegram-bot** - заменен на простые HTTP запросы
3. **Асинхронность** - полностью убрана из Telegram ботов
4. **Лишние файлы** - все бэкапы и старые версии удалены

### **🚀 ТЕПЕРЬ НОВЫЕ БОТЫ СОЗДАВАЙ ТАК:**
```python
# ТОЛЬКО ЭТОТ КОД ДЛЯ TELEGRAM БОТОВ:
import requests
import time
# ❌ НЕ ДОБАВЛЯЙ: asyncio, python-telegram-bot

# ✅ Простое логирование БЕЗ дублирования
import logging
logging.basicConfig(level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s',
                   handlers=[logging.FileHandler('/path/to/bot.log')])

BOT_TOKEN = "твой_токен"
def send_message(text):
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                  data={'chat_id': CHAT_ID, 'text': text})

while True:
    # опрос команд...
    time.sleep(1)  # НЕ asyncio.sleep()!
```

### **🔍 ИМЕНОВАНИЕ СЕРВИСОВ ДЛЯ АВТООБНАРУЖЕНИЯ:**
```bash
# ✅ ПРАВИЛЬНЫЕ ИМЕНА (обнаружатся автоматически):
my-new-bot.service
payment-webhook.service  
telegram-helper.service
amocrm-sync.service
health-monitor.service

# ❌ НЕПРАВИЛЬНЫЕ ИМЕНА (НЕ обнаружатся):
my-service.service
helper.service
sync.service
```

### **📊 СЕРВЕР В ИДЕАЛЬНОМ СОСТОЯНИИ:**
- **Порты**: 8000 (webhook), 8002 ❌УБРАН❌
- **Сервисы**: 5 активных, все стабильные
- **Автообнаружение**: 🔍 находит новые боты автоматически
- **Oracle Cloud**: в пределах лимитов
- **Диск**: очищен от лишних файлов
- **Логи**: чистые, БЕЗ дублирования, БЕЗ Event Loop ошибок
- **Ежедневные отчеты**: ⏰ в 9:00 утра с полной статистикой

**🏆 ГОТОВ К РАЗВЕРТЫВАНИЮ НОВЫХ БОТОВ С АВТООБНАРУЖЕНИЕМ!**

---

## 🧹 **АВТОМАТИЧЕСКАЯ ОЧИСТКА ЛОГОВ (ДОБАВЛЕНО 08.06.2025):**

### **🔄 Система ротации логов настроена:**

#### **📁 Локальная настройка (.gitignore):**
- ✅ Логи **исключены из git** (*.log, logs/, *.log.*)
- ✅ Временные файлы исключены (cache/, temp/, __pycache__/)
- ✅ Чувствительные данные защищены (*.env, *.key, *.pem)
- ✅ Webhook данные ограничены (только свежие)

#### **⚙️ Файлы автоочистки:**
1. **`cleanup_logs.py`** - основной скрипт очистки:
   - 🕒 Удаляет файлы старше **7 дней**
   - 📏 Ограничивает размер логов до **10 МБ**
   - 🧹 Очищает webhook JSON файлы
   - 📊 Ведет статистику очищенных файлов

2. **`setup_log_cleanup_cron.sh`** - установка автоматизации:
   - ⏰ Настраивает cron задачи на сервере
   - 🔧 Проверяет существующие задачи
   - 📝 Создает логи установки

3. **RotatingFileHandler в webhook_receiver.py:**
   - 🔄 Автоматическая ротация при достижении **5 МБ**
   - 📂 Сохраняет до **3 бэкап файлов**
   - ⚡ Работает в реальном времени

### **🕒 Cron задачи на сервере настроены:**
```bash
# Ежедневная очистка в 2:00 ночи
0 2 * * * cd /home/ubuntu/bots/amocrm_webhook && /usr/bin/python3 cleanup_logs.py

# Еженедельная очистка больших файлов в воскресенье в 3:00
0 3 * * 0 cd /home/ubuntu/bots/amocrm_webhook && /usr/bin/python3 cleanup_logs.py

# Существующий keep_alive каждый час
0 * * * * /home/ubuntu/keep_alive.sh
```

### **📋 Процедура развертывания автоочистки на новом сервере:**

#### **1️⃣ Копирование файлов:**
```bash
# С локальной машины на сервер
scp -i "/path/to/ssh-key.key" cleanup_logs.py setup_log_cleanup_cron.sh .gitignore ubuntu@SERVER_IP:~/bots/amocrm_webhook/
scp -i "/path/to/ssh-key.key" webhook_receiver.py ubuntu@SERVER_IP:~/bots/amocrm_webhook/
```

#### **2️⃣ Настройка на сервере:**
```bash
# Подключение к серверу
ssh -i "/path/to/ssh-key.key" ubuntu@SERVER_IP

# Переход в папку проекта
cd bots/amocrm_webhook

# Настройка автоочистки
bash setup_log_cleanup_cron.sh

# Тестовый запуск
python3 cleanup_logs.py

# Перезапуск сервиса с новой ротацией логов
sudo systemctl restart amocrm-webhook
sudo systemctl status amocrm-webhook --no-pager
```

#### **3️⃣ Проверка работы:**
```bash
# Проверить cron задачи
crontab -l

# Проверить логи очистки
cat cleanup_logs.log

# Проверить размер логов
ls -lh *.log

# Проверить работу ротации (через 5MB лог должен поделиться)
tail -f amocrm_webhook.log
```

### **🎯 Результаты автоочистки:**
- **🗑️ Удалено**: 17,017 файлов
- **💾 Освобождено**: 37.1 МБ места
- **📏 Размер логов**: Ограничен 5 МБ на файл
- **⏰ Автоматизация**: Ежедневно в 2:00, еженедельно больших файлов
- **🔒 Git чистота**: Логи больше не попадают в репозиторий

### **🚨 Важные примечания:**
1. **❌ НЕ УДАЛЯЙ** файлы webhook_data вручную - используй только автоочистку
2. **✅ ПРОВЕРЯЙ** размер логов регулярно: `du -sh *.log`
3. **⚠️ БЭКАПЫ** важных данных перед очисткой автоматически сохраняются
4. **📧 ЛОГИ ОЧИСТКИ** всегда сохраняются в `cleanup_logs.log`

**🎉 АВТООЧИСТКА ЛОГОВ ПОЛНОСТЬЮ НАСТРОЕНА И РАБОТАЕТ АВТОМАТИЧЕСКИ!**

---

## 🔄 **АВТООБНАРУЖЕНИЕ НОВЫХ БОТОВ И СИСТЕМА БЭКАПОВ (ДОБАВЛЕНО 08.06.2025):**

### **🎯 КРИТИЧЕСКИ ВАЖНО ДЛЯ НОВЫХ БОТОВ:**

#### **✅ ПРАВИЛЬНОЕ ИМЕНОВАНИЕ СЕРВИСОВ (ОБЯЗАТЕЛЬНО!):**
```bash
# 🟢 АВТОМАТИЧЕСКИ ОБНАРУЖАТСЯ (используй эти ключевые слова):
my-payment-bot.service       # содержит "bot"
server-monitor.service       # содержит "monitor"  
telegram-notifier.service    # содержит "telegram"
amocrm-integration.service   # содержит "amocrm"
order-webhook.service        # содержит "webhook"

# 🔴 НЕ БУДУТ ОБНАРУЖЕНЫ (избегай таких имен):
payment.service             # нет ключевых слов
notifier.service            # нет ключевых слов
integration.service         # нет ключевых слов
orders.service              # нет ключевых слов
my-app.service              # нет ключевых слов
```

#### **📁 ОБЯЗАТЕЛЬНАЯ СТРУКТУРА НОВЫХ БОТОВ:**
```bash
# ✅ ПРАВИЛЬНАЯ структура для автоматического бэкапа:
/home/ubuntu/bots/my_new_bot/     # папка ОБЯЗАТЕЛЬНО в bots/
├── bot.py                        # основной код
├── requirements.txt              # зависимости
├── .env                          # конфигурация (автоматически исключается из git)
├── logs/                         # логи (автоматически исключаются из бэкапа)
└── README.md                     # документация

# ❌ НЕПРАВИЛЬНО (НЕ попадет в бэкап):
/home/ubuntu/my_bot/              # НЕ в папке bots/
/opt/my_bot/                      # НЕ в папке bots/
/var/www/my_bot/                  # НЕ в папке bots/
```

### **🔍 АВТОМАТИЧЕСКОЕ ОБНАРУЖЕНИЕ РАБОТАЕТ ТАК:**

#### **🤖 Bot Monitor обнаруживает сервисы:**
```bash
# Команда автообнаружения (выполняется автоматически):
systemctl list-units --type=service --state=running | grep -E 'bot|monitor|telegram|amocrm|webhook'

# Результат: ALL новые боты с правильными именами появятся в отчетах!
```

#### **💾 Система бэкапов:**
```bash
# backup_server.py автоматически включает:
✅ ВСЮ папку /home/ubuntu/bots/ (включая новые боты)
✅ ВСЕ systemd сервисы с ключевыми словами
✅ Информацию о ВСЕХ установленных и активных сервисах
✅ Системные конфигурации новых сервисов

# restore_server.py автоматически:
✅ Обнаруживает ВСЕ сервисы ботов при остановке
✅ Восстанавливает ВСЕ файлы ботов
✅ Запускает ВСЕ найденные сервисы ботов
✅ Проверяет статус и показывает ошибки
```

### **🚀 ПРОЦЕДУРА РАЗВЕРТЫВАНИЯ НОВОГО БОТА:**

#### **1️⃣ СОЗДАНИЕ БОТА (следуй строго!):**
```bash
# Создай папку в правильном месте
mkdir -p /home/ubuntu/bots/my_new_bot

# Перенеси код
cd /home/ubuntu/bots/my_new_bot
# ... создай bot.py, requirements.txt, .env

# Установи зависимости
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### **2️⃣ СОЗДАНИЕ SYSTEMD СЕРВИСА (используй правильное имя!):**
```bash
# ✅ ОБЯЗАТЕЛЬНО используй ключевые слова в имени:
sudo nano /etc/systemd/system/my-new-bot.service

[Unit]
Description=My New Bot - автоматически обнаружится системой
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory=/home/ubuntu/bots/my_new_bot
ExecStart=/home/ubuntu/bots/my_new_bot/venv/bin/python bot.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

#### **3️⃣ ЗАПУСК И ПРОВЕРКА:**
```bash
# Перезагрузи systemd и запусти
sudo systemctl daemon-reload
sudo systemctl enable my-new-bot.service
sudo systemctl start my-new-bot.service

# Проверь статус
sudo systemctl status my-new-bot.service

# 🎉 ГОТОВО! Бот автоматически обнаружится системой мониторинга!
```

### **📊 АВТОМАТИЧЕСКАЯ ИНТЕГРАЦИЯ:**

#### **🔍 Что происходит автоматически после развертывания:**
```bash
# ✅ Bot Monitor автоматически:
- Обнаружит новый сервис при следующей проверке
- Включит его в ежедневные отчеты в 9:00
- Покажет в команде /status
- Добавит в статистику Oracle Cloud

# ✅ Система бэкапов автоматически:
- Включит новый бот в ежедневный бэкап в 3:00
- Заархивирует папку бота и systemd сервис
- Сможет восстановить при необходимости
- Остановит/запустит при восстановлении

# ✅ Система очистки логов автоматически:
- Будет очищать логи нового бота
- Исключит из git временные файлы
- Применит ротацию логов
```

### **🧪 ТЕСТИРОВАНИЕ СИСТЕМЫ:**

#### **🔍 Проверь автообнаружение:**
```bash
# Запусти тест системы бэкапов:
python3 test_new_bot_backup.py

# Проверь статус через Bot Monitor:
# Отправь /status в Telegram боту @sergei_dyshkant
```

#### **📋 Ожидаемые результаты тестирования:**
```
✅ Обнаружено X активных сервисов (включая новый)
✅ Обнаружено Y всего установленных сервисов
✅ Папка нового бота найдена в /home/ubuntu/bots/
✅ Systemd сервис найден в /etc/systemd/system/
✅ Автообнаружение: ✅ Работает
```

### **🚨 КРИТИЧЕСКИЕ ТРЕБОВАНИЯ:**

#### **❌ ЧТО НЕЛЬЗЯ ДЕЛАТЬ:**
```bash
❌ НЕ создавай боты вне папки /home/ubuntu/bots/
❌ НЕ используй имена сервисов без ключевых слов
❌ НЕ запускай боты под root
❌ НЕ используй asyncio в Telegram ботах (конфликты Event Loop)
❌ НЕ добавляй HTTP API в тот же процесс
```

#### **✅ ЧТО ОБЯЗАТЕЛЬНО ДЕЛАТЬ:**
```bash
✅ Используй ключевые слова: bot, monitor, telegram, amocrm, webhook
✅ Создавай боты в папке /home/ubuntu/bots/
✅ Используй простой синхронный код с requests
✅ Проверяй автообнаружение после развертывания
✅ Следи за ежедневными отчетами в 9:00
```

### **📈 СТАТИСТИКА ТЕКУЩЕЙ СИСТЕМЫ:**
```
🟢 5 активных сервисов ботов
📊 9 всего установленных сервисов  
📁 5 папок ботов в бэкапе
💾 Автоматический бэкап каждый день в 3:00
🧹 Автоочистка логов каждый день в 2:00
📱 Telegram отчеты каждый день в 9:00
☁️ iCloud синхронизация бэкапов
```

### **🔧 ФАЙЛЫ СИСТЕМЫ АВТООБНАРУЖЕНИЯ:**
```bash
# 💾 Система бэкапов:
backup_server.py              # создание полных бэкапов
restore_server.py             # восстановление из бэкапов  
setup_auto_backup.sh          # настройка автоматических бэкапов
test_new_bot_backup.py        # тестирование автообнаружения

# 🤖 Bot Monitor:
server_bot_monitor.py         # мониторинг всех ботов
# (использует те же принципы автообнаружения)
```

**🎯 РЕЗУЛЬТАТ: СИСТЕМА ПОЛНОСТЬЮ АВТОМАТИЧЕСКАЯ ДЛЯ НОВЫХ БОТОВ!**

**🚀 Просто следуй правилам именования и структуры - всё остальное работает автоматически!**