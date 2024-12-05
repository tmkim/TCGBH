'''
So let's take a minute to define what views we really need here.
The main views/pages that users will use:

    1. Welcome Page
        >> Button to go to view -> individual card lookup
        >> Button to go to view -> deck builder
        >> ???

    2. Individual Card Lookup Page
        >> Table component (list individual cards)
            - Search
            - Sort
            - Filter
        >> Detail component
            - Enlarged Card Image
            - Card Info
            - Market Price
    
    3. Deck Builder Page
        >> Table component (list individual cards) (same as #2)
        >> Table component (list cards added to the current deck)
            - Option to mark cards as purchased
        >> Deck Info component
            - Stats such as curve / number of cards per "cost"
            - Total market price to buy the entire deck
            
'''
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import generic
from .models import Deck, Card, Deck2Cards

class CardView(generic.ListView):
    template_name = "optcg/cards.html"
    context_object_name = "card_list"

    def get_queryset(self):
        return Card.objects.order_by("name")[:10]

class DeckView(generic.ListView):
    template_name = "optcg/decks.html"
    context_object_name = "deck_list"
    
    def get_queryset(self):
        return Deck.objects.order_by("owner")[:10]

# Example
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    return render(request, "optcg/index.html")

def welcome(request):
    return render(request, "optcg/welcome.html")

#Individual Card Lookup
# def cards(request):
#     card_list = Card.objects.order_by("name")[:10]
#     context = {"card_list": card_list}
#     return render(request, "optcg/cards.html", context)

#Deck Builder
# def decks(request):
#     deck_list = Deck.objects.order_by("owner")[:10]
#     context = {"deck_list": deck_list}
#     return render(request, "optcg/decks.html", context)