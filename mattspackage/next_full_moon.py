import ephem
from datetime import date, datetime

def next_full_moon(date_string):
    parsed_date = datetime.strptime(date_string, '%Y-%m-%d')
    return str(ephem.next_full_moon(parsed_date).datetime().date())

if __name__ == '__main__':
    today = str(date.today())
    print next_full_moon(today)
