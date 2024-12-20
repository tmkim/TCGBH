from rest_framework import serializers
from .models import Deck, Card, Deck2Cards
from django.contrib.auth.models import User

# class CardSerializer(serializers.HyperlinkedModelSerializer):
class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Card
        fields = ['url', 'id',  'name',  'imageUrl', 'tcgUrl'  'modifiedOn', 'marketPrice'] 
                #   'lowPrice',  'midPrice',  'highPrice',  'marketPrice',  
                #   'subTypeName',  'extRarity',  'extNumber',  'extDescription',  
                #   'extColor',  'extCardType',  'extLife',  'extPower',  'extSubtypes',  
                #   'extAttribute',  'extCost',  'extCounterplus']

# class DeckSerializer(serializers.HyperlinkedModelSerializer):
class DeckSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # cards = serializers.HyperlinkedRelatedField(many=True, view_name='card-detail', read_only=True)

    class Meta:
        model = Deck
        # fields = ['url', 'id', 'owner', 'cards']
        fields = ['id', 'name']


# class UserSerializer(serializers.HyperlinkedModelSerializer):
class UserSerializer(serializers.ModelSerializer):
    # decks = serializers.HyperlinkedRelatedField(many=True, view_name='deck-detail', read_only=True)
    # decks = serializers.RelatedField(many=True, view_name='deck-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username']

class Deck2CardsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deck2Cards
        fields = ['deck_id', 'card_id']