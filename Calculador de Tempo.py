def add_time(start, duration, day=False):
    week_day = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    start = start.replace(" ",":")

    hour_start, minute_start, period_start = start.split(":")
    hour_start, minute_start = int(hour_start), int(minute_start)
    start_in_minutes = (hour_start * 60) + minute_start

    hour_duration, minute_duration = duration.split(":")
    hour_duration, minute_duration =  int(hour_duration), int(minute_duration)
    duration_in_minutes = (hour_duration * 60) + minute_duration

    new_time_in_minutes = start_in_minutes + duration_in_minutes
    hour_new_time = new_time_in_minutes // 60 
    minutes_new_time = new_time_in_minutes % 60

    days = 0
    period_new_time = period_start

    if hour_new_time >= 12:
        if period_start == "PM":
            period_new_time = "AM"
            days = 1
        elif period_start == "AM":
            period_new_time = "PM"
     
    if hour_new_time >= 24:
        days = hour_new_time // 24
        if period_start == 'PM':
            days += 1
            hour_new_time -= 12
        if period_start == 'AM':
            hour_new_time -= 12
            period_new_time = "AM"

        how_many_days = f"{days} days later"

    if hour_new_time >= 13:
        hour_new_time = hour_new_time - 12
        
    if hour_new_time >= 24:
        hour_new_time -= 24 * (days - 1)

    if hour_new_time < 0:
        hour_new_time = hour_new_time + 12

    new_time = f"{hour_new_time:1}:{minutes_new_time:02} {period_new_time}"

    if day:
        day = day[0].upper() + day[1:].lower()
        index = week_day.index(day) + days
        new_week_day = week_day[index % len(week_day)]
        new_time += f", {new_week_day}"


    if days == 1:
        how_many_days = "next day"
    if days:
        new_time += f" ({how_many_days})"

    print(new_time)
    return new_time

add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)

add_time('2:59 AM', '24:00')
#return '2:59 AM (next day)'

add_time('2:59 AM', '24:00', 'saturDay')
#retornar '2:59 AM, Sunday (next day)'