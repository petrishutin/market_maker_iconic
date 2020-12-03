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
    """get BUY/SELL order book and returns price for 5 Max/Min () or 0 if size is not enough"""
    size = 5
    prices = list(order_book.keys())
    if not len(prices):
        return 0
    prices.sort(reverse=is_buy_orders)
    while order_book[prices[0]] < size:
        size -= order_book[prices[0]]
        prices = prices[1:]
        if not prices:
            return 0
    return prices[0]


def count_size_5_spread(sell_orders_book: dict, buy_orders_book: dict) -> int:
    """Count and return spread for size 5 orders. """
    sell_minimal_price = get_5_orders(sell_orders_book)
    buy_maximal_price = get_5_orders(buy_orders_book, is_buy_orders=True)
    if not sell_minimal_price and not buy_maximal_price:
        return 0
    best_sell_price = best_price(sell_orders_book)
    best_buy_price = best_price(buy_orders_book)
    avg_price = (best_sell_price + best_buy_price) / 2
    spread = (sell_minimal_price - buy_maximal_price) / avg_price * 10000
    return spread


def best_price(order_book, is_buy_price=False):
    prices = list(order_book.keys())
    if not len(prices):
        return 0
    prices.sort(reverse=is_buy_price)
    return prices[0]


if __name__ == '__main__':
    sell_order_book = {11.0: 5, 10.5: 3}
    buy_order_book = {9.5: 5}
    result = count_size_5_spread(sell_order_book, buy_order_book)
    print(result)
