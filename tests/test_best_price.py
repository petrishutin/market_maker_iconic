import pytest
from check_market_maker import best_price


def test_minimal_sell_price():
    order_book = {
        10.0: 5,
        11.0: 5
    }
    result = best_price(order_book)
    assert result == 10.0


def test_maximal_price():
    order_book = {
        10.0: 5,
        11.0: 5
    }
    result = best_price(order_book, is_buy_price=True)
    assert result == 11.0
