from django.test import TestCase
from .models import Card

# Create your tests here.
class CardModelTests(TestCase):
    def test_card_has_market_price(self):
        free_card = Card(market_price=0)
        self.assertIs(free_card.has_market_price(), False)

    def test_card_has_no_market_price(self):
        free_card = Card(market_price=420)
        self.assertIs(free_card.has_market_price(), True)