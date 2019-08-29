"""Main."""
import buyer.settings as settings
from buyer.notify import notify
from buyer.exchange import exchange


if __name__ == '__main__':
    # read settings
    settings = settings.load('./buyer/settings.yml')
    # set token to notifier
    notify.set_line_token(settings['notify']['line']['token'])
    # initialize exchange
    exchange = exchange.ExchangeController(settings['exchange'])
    # buy process
    amount = exchange.compute_amount()
    exchange.buy(amount)
