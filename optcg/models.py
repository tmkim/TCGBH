from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

class Deck(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Deck '{0}', built by '{1}'".format(self.name, self.owner)
    
    @admin.display(
        boolean=True,
        ordering="owner",
        description="Deck",
    )

    def get_info(self):
        return {
            'owner': self.owner,
            'name': self.name
        }

class Card(models.Model):
    name = models.CharField(max_length=200)
    cost = models.IntegerField(default=0)
    color = models.CharField(max_length=200)
    rarity = models.CharField(max_length=200)
    desc = models.CharField(max_length=420)
    market_price = models.DecimalField(decimal_places=2, max_digits=15)
    # Will add more fields later

    def __str__(self):
        return "{0} Cost {1} {2} --> {3}".format(self.cost, self.color, self.name, self.market_price)
    
    @admin.display(
        boolean=True,
        ordering="name",
        description="Card",
    )
    
    def get_info(self):
        return {
            'name' : self.name,
            'market_price' :self.market_price,
            'rarity': self.rarity,
            'desc': self.desc,
            'color': self.color,
            'cost': self.cost,
        }

class Deck2Cards(models.Model):
    deck_id = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} -- {1}".format(self.deck_id, self.card_id)