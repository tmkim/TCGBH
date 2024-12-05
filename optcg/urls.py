from django.urls import path

from . import views

app_name = "optcg"
# ex: path("<int:question_id>/vote/", views.vote, name="vote"),
urlpatterns = [
    path("", views.index, name="index"),
    path("welcome/", views.welcome, name="welcome"),
    path("cards/", views.CardView.as_view(), name="cards"),
    path("decks/", views.DeckView.as_view(), name="decks")
]