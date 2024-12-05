# TCGBH
Trading Card Game - Bounty Hunter : Useful app for calculating the market price for several trading cards

The goal is to provide an app to help users calculate the cost of building a deck for the [One Piece] TCG, using information from TCGPlayer via https://tcgcsv.com/
End goal is similar to a combination of Egman Deckbuilder + TCG Player market prices
This may help users finance their own decks, keep track of what cards they already own, and calculate the cost of decks seen in competitive play.
Extra: Users may save price data for future comparisons

Users will not have to log in for basic functionality. Login will allow for extra features such as saving cards/decks.

Users will be able to : 
    - Create a deck list
        > Build a deck using the list of existing cards 
        > Import a deck list using the format from the One Piece TCG Simulator
    - See the price of individual cards
    - See the price of all cards in a deck
    - Mark off which cards they have purchased to see how much the remaining cards will cost

Functional Requirements : 
    - Efficiently parse CSV files from tcgcsv 
    - Update database of cards + prices (around 20:00:00 UTC daily)
    - Users may build a list of cards 
    - Users may view the current price of cards 
    - 

Nonfunctional Requirements : 
    - Database is updated at regular intervals (around 20:00:00 UTC daily)
    - Data is consistent 
    - There are many cards available, so we want to make sure they can be loaded quickly

APIs : 
    - GET data from tcgcsv.com 
    - POST to database (card info, price info)
    - UPDATE database (price updates)
    
    - GET card info from database 
    - POST deck list 
    - UPDATE deck list 

Tables : 
    - Users [id, name, pw, email, etc]
    - Cards [id, name, ?image?, card info, price]
    - Decklists [id, user, name, cards included, total price]
    - Decklists_Cards [deck_id, card_id]