import datetime

def first_day_of_month(year, first_day_of_year):

    first_days_of_month = []


    for month in range(1, 13):

        first_day = datetime.date(year, month, 1)
        day_name = first_day.strftime("%A")
        first_days_of_month.append(f"{first_day.strftime('%B')} 1, {year} is {day_name}")
    return first_days_of_month

year = 2021
first_day_of_year = 5 # Friday
z=first_day_of_month(year, first_day_of_year)
for txt in z:
    print(txt)