import pytest
from check_market_maker import get_5_orders

class TestGetFiveOrders:
    def test_get_5_orders_price(self):
        order_book = {10.0: 5}
        result = get_5_orders(order_book)
        assert result == 10.0

    def test_get_5_sell_orders_lowest_price(self):
        sell_order_book = {11.0: 5, 10.0: 5}
        result = get_5_orders(sell_order_book)
        assert result == 10.0

    def test_get_5_buy_orders_highest_price(self):
        buy_order_book = {11.0: 5, 10.0: 5}
        result = get_5_orders(buy_order_book, is_buy_orders=True)
        assert result == 11.0

    def test_get_5_sell_orders_price_with_size_smaller_than_5(self):
        order_book = {
            10.0: 1,
            11.0: 1,
            12.0: 1,
            13.0: 1,
            14.0: 1,
        }
        result = get_5_orders(order_book)
        assert result == 14.0

    def test_get_5_buy_orders_price_with_size_smaller_than_5(self):
        order_book = {
            10.0: 1,
            11.0: 1,
            12.0: 1,
            13.0: 1,
            14.0: 1,
        }
        result = get_5_orders(order_book, is_buy_orders=True)
        assert result == 10.0

    def test_not_enough_size(self):
        order_book = {
            10.0: 1,
            11.0: 1
        }
        result = get_5_orders(order_book)
        assert not result