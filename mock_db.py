from random import randint
from datetime import datetime, timedelta
from pprint import pprint


def get_data_from_db(account_id, date, number_or_lines=100):
    """Returns mocked data from DB"""
    mocked_data = []
    date = datetime.strptime(date, '%Y-%m-%d')
    seconds_to_increment = 86400 // number_or_lines
    time_inc = timedelta(hours=0, minutes=0, seconds=seconds_to_increment)
    for line in range(number_or_lines):
        side = random_side()
        price = random_price(side)
        size = randint(0, 6)
        mocked_data.append((line + 1, account_id, str(date), side, price, size))
        date += time_inc
    return mocked_data


def random_price(side):
    price = 10 + randint(0, 9) / 10
    if side == 'SELL':
        return price + 0.5
    return price


def random_side():
    side = randint(0, 1)
    return 'BUY' if side else 'SELL'


if __name__ == '__main__':
    result = get_data_from_db(1, '2020-12-1')
    pprint(result)
