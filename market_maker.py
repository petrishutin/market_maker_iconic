"""CLI app for check_market_maker"""

import argparse
from check_market_maker import check_market_maker


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--account', type=int, help="Account_id to check, must be valid for account_id;")
    parser.add_argument('-d', '--date', type=str, help="Input date in format 'YYYY-MM-DD'")
    args = parser.parse_args()
    account_id = args.account
    date = args.date
    result = check_market_maker(account_id, date)
    print(result)


if __name__ == '__main__':
    main()
