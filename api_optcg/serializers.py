from rest_framework import serializers
from .models import Deck, Card
from django.contrib.auth.models import User

class CardSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Deck
        fields = ['url', 'id',  'name',  'imageUrl', 'tcgUrl'  'modifiedOn', 'marketPrice'] 
                #   'lowPrice',  'midPrice',  'highPrice',  'marketPrice',  
                #   'subTypeName',  'extRarity',  'extNumber',  'extDescription',  
                #   'extColor',  'extCardType',  'extLife',  'extPower',  'extSubtypes',  
                #   'extAttribute',  'extCost',  'extCounterplus']

class DeckSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # cards = serializers.HyperlinkedRelatedField(many=True, view_name='card-detail', read_only=True)

    class Meta:
        model = Deck
        # fields = ['url', 'id', 'owner', 'cards']
        fields = ['url', 'id', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    decks = serializers.HyperlinkedRelatedField(many=True, view_name='deck-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'decks']