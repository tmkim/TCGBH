from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'decks', views.DeckViewSet, basename='deck')
router.register(r'cards', views.CardViewSet, basename='card')
router.register(r'deck2cards', views.Deck2CardsViewSet, basename='deck2cards')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
