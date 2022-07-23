import re
from queue import SimpleQueue


def daysWeek(days_pass: int, day: str) -> str:
    """Функция возвращает день недели который будет через days_pass дней начиная отсчет от day.

    Args:
        days_pass (int): Сколько дней прошло
        day (str): День от которого отсчитываем

    Returns:
        str: День недели который будет через days_pass дней начиная отсчет от day
    """

    week = [
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",
    ]
    days_pass += week.index(
        day.lower()
    )  # смещаю начало очереди на день переданный в функцию
    queue = SimpleQueue()
    for day_name in week:
        queue.put(day_name)
    for i in range(days_pass):
        queue.put(queue.get())
    return queue.get().capitalize()


def add_time(start, duration, day_of_the_week=None):
    times_of_day = re.search(r"[AM,PM].", start).group(0)
    hour = re.findall(r"\d+", start)[0]
    minute = re.findall(r"\d+", start)[1]
    add_hour = re.findall(r"\d+", duration)[0]
    add_minute = re.findall(r"\d+", duration)[1]

    answer_hour = int(hour) + int(add_hour)
    answer_minute = int(minute) + int(add_minute)

    while answer_minute >= 60:
        answer_minute -= 60
        answer_hour += 1
    if answer_minute < 10:
        answer_minute = f"0{answer_minute}"
    elif answer_minute == 0:
        answer_minute = "00"

    days = 0
    while answer_hour >= 12:
        answer_hour -= 12
        days += 0.5
        if times_of_day == "AM":
            times_of_day = "PM"
        else:
            times_of_day = "AM"

    if answer_hour == 0:
        answer_hour = 12

    if day_of_the_week:
        if days > 1.0:
            return (
                str(answer_hour)
                + ":"
                + str(answer_minute)
                + " "
                + times_of_day
                + ", "
                + daysWeek(round(days), day_of_the_week)
                + " ("
                + str(round(days))
                + " days later)"
            )
        elif days >= 0.5 and times_of_day == "AM":
            return (
                str(answer_hour)
                + ":"
                + str(answer_minute)
                + " "
                + times_of_day
                + ", "
                + daysWeek(round(days), day_of_the_week)
                + " (next day)"
            )
        else:
            return (
                str(answer_hour)
                + ":"
                + str(answer_minute)
                + " "
                + times_of_day
                + f", {day_of_the_week}"
            )
    else:
        if days > 1.0:
            return (
                str(answer_hour)
                + ":"
                + str(answer_minute)
                + " "
                + times_of_day
                + " ("
                + str(round(days))
                + " days later)"
            )
        elif days >= 0.5 and times_of_day == "AM":
            return (
                str(answer_hour)
                + ":"
                + str(answer_minute)
                + " "
                + times_of_day
                + " (next day)"
            )
        else:
            return str(answer_hour) + ":" + str(answer_minute) + " " + times_of_day
