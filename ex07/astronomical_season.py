from datetime import date


def astronomical_season(dateArg):
    month_name_to_month_number = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }
    day = dateArg[0]
    month = dateArg[1]
    month = month_name_to_month_number[month]
    calcdate = date(2023, month, day)
    if calcdate >= date(2023, 12, 21) and calcdate < date(2023, 1, 1):
        return "winter"
    if calcdate >= date(2023, 1, 1) and calcdate < date(2023, 3, 20):
        return "winter"
    if calcdate >= date(2023, 3, 20) and calcdate < date(2023, 6, 21):
        return "spring"
    if calcdate >= date(2023, 6, 21) and calcdate < date(2023, 9, 23):
        return "summer"
    if calcdate >= date(2023, 9, 23) and calcdate < date(2023, 12, 21):
        return "autumn"


print(astronomical_season((20, "mar")))
print(astronomical_season((21, "mar")))
print(astronomical_season((1, "jan")))
