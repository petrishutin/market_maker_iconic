from mock_db import get_data_from_db


def check_market_maker(account_id: int, date: str) -> str:
    """This function calculates how long market maker program terms were being complied for specific date"""
    data_for_date: list = get_data_from_db(account_id, date)
    data_for_date.sort(key=lambda x: x[2])
    acctual_buy_orders = {}
    acctual_sell_orders = {}
    for line in data_for_date:
        # updating orders books
        if line[3] == 'SELL':
            acctual_sell_orders.update({line[4]: line[5]})
        else:
            acctual_buy_orders.update({line[4]: line[5]})

    return str(data_for_date)


def get_5_orders(order_book, is_buy_orders=False) -> float:
    """get BUY/SELL order book and returns price for 5 Max/Min ()"""
    size = 5
    prices = list(order_book.keys())
    prices.sort(reverse=is_buy_orders)
    while order_book[prices[0]] < size:
        size -= order_book[prices[0]]
        prices = prices[1:]
        if not prices:
            return 0
    return prices[0]


def count_size_5_spread(sell_orders_book, buy_orders_book):
    pass


if __name__ == '__main__':
    order_book = {11.0: 5, 10.0: 5}
    result = get_5_orders(order_book)
    print(result)
