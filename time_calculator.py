def add_time(start, duration, day=False):
    days = {'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5,
            'saturday':6, 'sunday':7}
    days_index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday',
                'Saturday', 'Sunday']       

    hours = int(start.split(':')[0])
    minutes_raw = start.split(':')[1]
    minutes = int(minutes_raw.split(' ')[0])
    am_pm = start.split(' ')[1]

    hour_add = int(duration.split(':')[0])
    min_add = int(duration.split(':')[1])

    hour_sum = hours + hour_add
    min_sum = minutes + min_add
    days_later = 0 
    am_pm_end = am_pm
    day_end_num = 0
    day_end = ''
    days_after = ''

    if min_sum >= 60:
        hour_sum += 1
        min_sum = min_sum - 60

    hour_end = hour_sum

    if hour_end >= 12:
        hour_end = hour_end % 12
    if hour_end == 0:
        hour_end = 12 

    am_pm_switches = int(hour_sum / 12)
    
    if am_pm == 'AM':
        days_later = int(hour_sum / 24) 
        if days_later < 0:
            days_later = 0
    if am_pm == 'PM':
        days_later = int((hour_sum + 12) / 24)        

    if am_pm == 'AM' and (am_pm_switches % 2) == 1:
        am_pm_end = 'PM'
    if am_pm == 'PM' and (am_pm_switches % 2) == 1:
        am_pm_end = 'AM' 

    if min_sum < 10:
        min_sum = '0' + str(min_sum)     

    if days_later == 1:
        days_after = ' (next day)'   
    if days_later > 1:
        days_after = ' ({} days later)'.format(days_later)     

    if day:
        day = day.lower()
        day_end_num = (int(days[day] + days_later) % 7) - 1 
        day_end = ', ' + days_index[day_end_num]

    new_time = str(hour_end) + ':' + str(min_sum) + ' ' + am_pm_end + day_end + days_after


    return new_time