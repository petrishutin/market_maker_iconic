from mock_db import get_data_from_db

def check_market_maker(account_id: int, date: str) -> str:
    data_for_date = get_data_from_db(account_id, date)
    return str(data_for_date)

if __name__ == '__main__':
    check_market_maker(1, '2020-12-1')


