from django.contrib import admin
from .models import Deck, Card

class CardAdmin(admin.ModelAdmin):
    # fields = ['name', 'cost', 'color', 'rarity', 'desc', 'market_price']
    fieldsets = [
        ("Primary Info", {"fields": ['name', 'cost', 'color', 'market_price']}),
        ("Secondary Info", {"fields": ['rarity', 'desc',]})
    ]
    list_display = ['name', 'cost', 'color', 'market_price']
    search_fields = ['name']

# Use this to link models with foreign keys
# class CardInline(admin.StackedInline // admin.TabularInline):
#     model = Card 
#     extra = 5

class DeckAdmin(admin.ModelAdmin):
    fields = ['owner', 'name']
    search_fields = ['owner']
    # inlines = [CardInline]

# Register your models here.
admin.site.register(Deck, DeckAdmin)
admin.site.register(Card, CardAdmin)