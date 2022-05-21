import re

week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def add_time(start, duration, day_of_the_week=None):
    times_of_day = re.search(r'[AM,PM].', start).group(0)
    hour = re.findall(r'\d+', start)[0]
    minute = re.findall(r'\d+', start)[1]
    add_hour = re.findall(r'\d+', duration)[0]
    add_minute = re.findall(r'\d+', duration)[1]

    answer_hour = int(hour) + int(add_hour)
    answer_minute = int(minute) + int(add_minute)

    while answer_minute >= 60:
        answer_minute -= 60
        answer_hour += 1
    if answer_minute < 10:
        answer_minute = f'0{answer_minute}'
    elif answer_minute == 0:
        answer_minute = '00'

    days = 0
    while answer_hour >= 12:
        answer_hour -= 12
        days += 0.5
        if times_of_day == 'AM':
            times_of_day = 'PM'
        else:
            times_of_day = 'AM'

    if answer_hour == 0:
        answer_hour = 12

    if day_of_the_week:
        if days > 1.0:
            return str(answer_hour) + ':' + str(answer_minute) + \
                   ' ' + times_of_day + ', ' + week[
                       week.index(f'{day_of_the_week}'.lower()) + round(days) % 7 if round(
                           days) % 7 != 6 else round(days) % 7 - 6].capitalize() + ' (' + str(
                round(days)) + ' days later)'
        elif days >= 0.5 and times_of_day == 'AM':
            return str(answer_hour) + ':' + str(
                answer_minute) + ' ' + times_of_day + ', ' + week[
                       week.index(f'{day_of_the_week}'.lower()) + 1].capitalize() + ' (next day)'
        else:
            return str(answer_hour) + ':' + str(answer_minute) + ' ' + times_of_day + f', {day_of_the_week}'
    else:
        if days > 1.0:
            return str(answer_hour) + ':' + str(answer_minute) + ' ' + times_of_day + ' (' + str(
                round(days)) + ' days later)'
        elif days >= 0.5 and times_of_day == 'AM':
            return str(answer_hour) + ':' + str(answer_minute) + ' ' + times_of_day + ' (next day)'
        else:
            return str(answer_hour) + ':' + str(answer_minute) + ' ' + times_of_day
