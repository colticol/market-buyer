"""Test Settings."""
import unittest
from buyer.settings import load


class TestSettings(unittest.TestCase):
    """Settings test cases."""

    def test_load(self):
        """Test load yaml."""
        settings = load('./tests/settings.yml')
        self.assertEqual('bitflyer', settings['exchange']['name'])
        self.assertEqual('key', settings['exchange']['api_key'])
        self.assertEqual('secret', settings['exchange']['api_secret'])
        self.assertEqual('BTC/JPY', settings['exchange']['symbol'])
        self.assertEqual(1000, settings['exchange']['yen'])
        self.assertEqual('token', settings['notify']['line']['token'])


if __name__ == '__main__':
    unittest.main()
