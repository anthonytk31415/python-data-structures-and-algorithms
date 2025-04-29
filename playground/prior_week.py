

import datetime
# from datetime import datetime, timedelta

# def get_last_week_date_range(date): 
#     '''Given a date, return the start and end dates of the last week (Sunday to Saturday).'''
#     # Get to the start of the current week (Monday)
#     start_of_current_week = date - timedelta(days=date.weekday())
#     # Go back 7 days to get to last week's Sunday
#     start_date = start_of_current_week - timedelta(days=7)
#     # Add 6 days to get to last week's Saturday
#     end_date = start_date + timedelta(days=6)
#     return start_date, end_date


def get_last_week_range(date):
    weekdate_num = (date.weekday() + 1)%7    
    last_sun = date + datetime.timedelta(days=- weekdate_num - 7)
    last_sat = last_sun + datetime.timedelta(days=6)    
    return last_sun, last_sat


def get_current_week_range(date):
    weekdate_num = (date.weekday() + 1)%7    
    cur_sun = date + datetime.timedelta(days=- weekdate_num)
    cur_sat = cur_sun + datetime.timedelta(days=6)    
    return cur_sun, cur_sat



# date2 = datetime.datetime(2025, 4, 3)   # April 3, 2025
date2 = datetime.datetime(2025, 4, 3)   # April 3, 2025
# print(get_last_week_range(date2))

print(get_current_week_range(date2))

# date1 = datetime(2025, 4, 26)  # April 26, 2025



# print(get_last_week_date_range(date1))
# print(get_last_week_date_range(date2))