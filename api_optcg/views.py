from .models import Deck, Card, Deck2Cards
from .serializers import DeckSerializer, CardSerializer, UserSerializer, Deck2CardsSerializer
# from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'cards': reverse('card-list', request=request, format=format),
        'decks': reverse('deck-list', request=request, format=format)
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeckViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

class CardViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

class Deck2CardsViewSet(viewsets.ModelViewSet):
    queryset = Deck2Cards.objects.all()
    serializer_class = Deck2CardsSerializer