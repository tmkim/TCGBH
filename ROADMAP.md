# Development Road Map

* This app will eventually be available for ALL TCG, but starting with One Piece then expanding.

- Set up virtual environment with Django, Postgresql
- Set up database tables/models
- User Authentication
- Daily updates via tcgcsv.com
    > Download csv
    > Update database with values
    > 
- Individual Card view
    > List all cards in a table with info + market price
    > Users can click card to see larger details
    > Search Function
    > Filter Function
    > Sort Function
    >

- Deck builder view
    > Similar to IC view, but lets you add/remove from a "deck"
    > Users can save decks and easily load them
    > Users can import/export following OP Sim format
    >

- Consider using ElasticSearch for card search