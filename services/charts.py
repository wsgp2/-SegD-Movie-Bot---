import os
import matplotlib
matplotlib.use('Agg')  # Используем backend без GUI для сервера
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import matplotlib.dates as mdates

async def generate_charts_for_user(db, user_id, windows=[7, 30, 90, 365], tmp_dir='tmp'):
    """
    Генерация графиков просмотров для пользователя.
    Графики сохраняются в PNG в tmp_dir.
    """
    paths = []
    os.makedirs(tmp_dir, exist_ok=True)

    for days in windows:
        rows = await db.get_movies_count_by_day(user_id, days)  # [(display_day, count)]
        plt.figure(figsize=(10, 6))

        if not rows:
            # Пустой график
            plt.text(0.5, 0.5, 'Нет данных', ha='center', va='center', fontsize=16)
            plt.title(f'Просмотры за последние {days} дней')
            plt.axis('off')
        else:
            # Конвертируем строки 'DD.MM.YYYY 00:00' обратно в datetime
            dates = [datetime.strptime(r[0], '%d.%m.%Y %H:%M') for r in rows]
            counts = [int(r[1]) for r in rows]

            if days <= 30:
                # Для коротких периодов: линии по дням
                plt.plot(dates, counts, marker='o', linestyle='-', color='tab:blue')
                plt.gca().xaxis.set_major_locator(mdates.DayLocator())
                plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))
            elif days <= 90:
                # Для 90 дней: группировка по неделям
                week_data = {}
                for date, count in zip(dates, counts):
                    week_start = date - timedelta(days=date.weekday())
                    week_data[week_start] = week_data.get(week_start, 0) + count
                week_dates = sorted(week_data.keys())
                week_counts = [week_data[d] for d in week_dates]
                plt.bar(week_dates, week_counts, width=5, color='tab:orange')
                plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d.%m'))
            else:
                # Для 365 дней: группировка по месяцам
                month_data = {}
                for date, count in zip(dates, counts):
                    month_start = datetime(date.year, date.month, 1)
                    month_data[month_start] = month_data.get(month_start, 0) + count
                month_dates = sorted(month_data.keys())
                month_counts = [month_data[d] for d in month_dates]
                plt.bar(month_dates, month_counts, width=20, color='tab:green')
                plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))  # Янв, Фев и т.д.

            # Настройки для всех графиков
            plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))  # только целые числа на Y
            plt.title(f'Просмотры за последние {days} дней', fontsize=14)
            plt.ylabel('Количество фильмов')
            plt.grid(True, alpha=0.3)
            plt.xticks(rotation=45, fontsize=9)
            plt.tight_layout()

        # Сохраняем график
        fname = os.path.join(tmp_dir, f'chart_{user_id}_{days}d.png')
        plt.savefig(fname)
        plt.close()
        paths.append(fname)

    return paths
