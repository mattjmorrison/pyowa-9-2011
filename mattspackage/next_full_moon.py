import ephem
from datetime import date, datetime

DATE_FORMAT = "%Y-%m-%d"

def next_full_moon(date_string):
    parsed_date = datetime.strptime(date_string, DATE_FORMAT)
    next_full_moon_date = ephem.next_full_moon(parsed_date).datetime()
    return next_full_moon_date.strftime(DATE_FORMAT)

if __name__ == '__main__':
    today = str(date.today())
    print next_full_moon(today)
