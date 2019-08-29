"""Test Exchange."""
import unittest
import ccxt
from mock import Mock
from buyer.exchange import exchange


class TestExchange(unittest.TestCase):
    """Exchange test cases."""

    def test_compute_amount_simple_case(self):
        """Test compute amount (simple_case)."""
        settings = {'symbol': 'BTC/JPY', 'yen': 1000}
        bitflyer = ccxt.bitflyer()
        bitflyer.fetch_order_book = Mock()
        bitflyer.fetch_order_book.return_value = {
            'asks': [[1000000., 0.1], [1010000., 0.1]]
        }
        controller = exchange.ExchangeController(settings, exchange=bitflyer)

        amount = controller.compute_amount()
        bitflyer.fetch_order_book.assert_called_once_with('BTC/JPY')
        self.assertEqual(0.001, amount)

    def test_compute_amount_complex_case(self):
        """Test compute amount (complex case)."""
        settings = {'symbol': 'BTC/JPY', 'yen': 9000}
        bitflyer = ccxt.bitflyer()
        bitflyer.fetch_order_book = Mock()
        bitflyer.fetch_order_book.return_value = {
            'asks': [[1000000., 0.001], [2000000., 0.1]]
        }
        controller = exchange.ExchangeController(settings, exchange=bitflyer)

        amount = controller.compute_amount()
        bitflyer.fetch_order_book.assert_called_once_with('BTC/JPY')
        self.assertEqual(0.005, amount)

    def test_compute_amount_error(self):
        """Test compute amount with error."""
        settings = {'symbol': 'BTC/JPY', 'yen': 1000}
        bitflyer = ccxt.bitflyer()
        bitflyer.fetch_order_book = Mock()
        bitflyer.fetch_order_book.side_effect = Exception("mock excepton")
        controller = exchange.ExchangeController(settings, exchange=bitflyer)

        with self.assertRaises(Exception):
            controller.compute_amount()
        bitflyer.fetch_order_book.assert_called_once_with('BTC/JPY')

    def test_buy(self):
        """Test buy."""
        settings = {'symbol': 'BTC/JPY', 'yen': 1000}
        bitflyer = ccxt.bitflyer()
        bitflyer.create_market_buy_order = Mock()
        controller = exchange.ExchangeController(settings, exchange=bitflyer)

        amount = 0.1
        controller.buy(amount)
        bitflyer.create_market_buy_order.assert_called_once_with('BTC/JPY', amount)

    def test_buy_error(self):
        """Test buy with error."""
        settings = {'symbol': 'BTC/JPY', 'yen': 1000}
        bitflyer = ccxt.bitflyer()
        bitflyer.create_market_buy_order = Mock()
        bitflyer.create_market_buy_order.side_effect = Exception("mock exception")
        controller = exchange.ExchangeController(settings, exchange=bitflyer)

        amount = 0.1
        with self.assertRaises(Exception):
            controller.buy(amount)
        bitflyer.create_market_buy_order.assert_called_once_with('BTC/JPY', amount)


if __name__ == '__main__':
    unittest.main()
