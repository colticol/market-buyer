"""Exchange Pack."""
import ccxt
from buyer.notify import notify


class ExchangeController(object):
    """Exchange Controller."""

    def __init__(self, settings, exchange=None):
        """Initialize."""
        if exchange is None:
            self.__exchange = eval('ccxt.{0}()'.format(settings['name']))
            self.__exchange.apiKey = settings['api_key']
            self.__exchange.secret = settings['api_secret']
        else:
            self.__exchange = exchange
        self.__symbol = settings['symbol']
        self.__yen = settings['yen']

    def compute_amount(self):
        """Convert yen to currency amount."""
        rest = self.__yen
        out = 0.0
        # fetch order book
        try:
            order_book = self.__exchange.fetch_order_book(self.__symbol)
        except ccxt.NetworkError as e:
            self.__notify('fetch_order_book failed due to a network error:' + str(e))
            raise e
        except ccxt.ExchangeError as e:
            self.__notify('fetch_order_book failed due to exchange error:' + str(e))
            raise e
        except Exception as e:
            self.__notify('fetch_order_book failed with:', str(e))
            raise e
        # compute amount
        for price, amount in order_book['asks']:
            if rest <= 0.0:
                break
            fee = min(rest, price * amount)
            out += fee / price
            rest -= fee
        return out

    def buy(self, amount):
        """Buy according to settings."""
        try:
            self.__exchange.create_market_buy_order(self.__symbol, amount)
        except ccxt.NetworkError as e:
            self.__notify('create_market_buy_order failed due to a network error:' + str(e))
            raise e
        except ccxt.ExchangeError as e:
            self.__notify('create_market_buy_order failed due to exchange error:' + str(e))
            raise e
        except Exception as e:
            self.__notify('create_market_buy_order failed with:' + str(e))
            raise e
        # notify result
        self.__notify('buy [symbol][{0}][amount][{1}]'.format(self.__symbol, amount))

    def __notify(self, message):
        notify.notify_line(message)
