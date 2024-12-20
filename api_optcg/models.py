from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

class Deck(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    created = models.DateTimeField("Date Created")
    modified = models.DateTimeField("Last Modified")
    
    class Meta:
        ordering = ['created']

class Card(models.Model):
    name = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200) # url?
    tcgUrl = models.CharField(max_length=200)
    modifiedOn = models.DateTimeField("Last Modified")
    # lowPrice = models.DecimalField(decimal_places=2, max_digits=12)
    # midPrice = models.DecimalField(decimal_places=2, max_digits=12)
    # highPrice = models.DecimalField(decimal_places=2, max_digits=12)
    marketPrice = models.DecimalField(decimal_places=2, max_digits=12)
    # subTypeName = models.CharField(max_length=200)
    # extRarity = models.CharField(max_length=5)
    # extNumber = models.CharField(max_length=10)
    # extDescription = models.CharField(max_length=420)
    # extColor = models.CharField(max_length=20)
    # extCardType = models.CharField(max_length=20)
    # extLife = models.IntegerField(default=0)
    # extPower = models.IntegerField(default=0)
    # extSubtypes = models.CharField(max_length=100)
    # extAttribute = models.CharField(max_length=20)
    # extCost = models.IntegerField(default=0)
    # extCounterplus = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['name']

class Deck2Cards(models.Model):
    deck_id = models.ForeignKey(Deck, on_delete=models.CASCADE)
    card_id = models.ForeignKey(Card, on_delete=models.CASCADE)

    class Meta:
        ordering = ['deck_id']

#     def __str__(self):
#         return "{0} -- {1}".format(self.deck_id, self.card_id)