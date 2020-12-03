import pytest
from check_market_maker import count_size_5_spread


def test_spread():
    sell_order_book = {10.5: 5}
    buy_order_book = {9.5: 5}
    result = count_size_5_spread(sell_order_book, buy_order_book)
    assert result == 1000


def test_spread_with_low_sizes():
    sell_order_book = {10.5: 5}
    buy_order_book = {9.5: 5}
    result = count_size_5_spread(sell_order_book, buy_order_book)
    assert result == 1500
