def is_leap(year):
    if year % 4 == 0:
        if year % 100 ==0:
            if year %400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(years,months):
    if months > 12:
        return 'please enter correct value for months'
    month_days = [31,28,31,30,31,31,30,31,30,31,30,31]
    if is_leap(years) and months == 2:
        month_days[2] = 29
    return month_days[months]

print(days_in_month(int(input('please enter year')),int(input('please enter month'))))
