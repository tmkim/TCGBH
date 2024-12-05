# Development Log

MM/DD/YYYY:
    > Daily Objective:
        - 
    > Progress:
        - 
    > TODO:
        - 

12/04/2024:
    > Daily Objective:
        - Set up Dev Log, Road Map, Read Me
        - Set up Environment (django, postgresql)
            - Initialize Django project
            - Set up DB connection

    > Progress:
        - Set up Dev Log, Road Map, Read Me

        - Set up Environment (django, postgresql)
            - Initialize Django project
                > Project - TCGBH/bountyhunter
                    ~ bountyhunter/urls.py
                > App - TCGBH/optcg
                    ~ optcg/views.py
                    ~ optcg/urls.py

            - Set up DB connection
                > $pip install django
                > $pip install postgres
                    > bountyhunter/settings.py
                    > cdt/.pg_pass -> $chmod 600 .pgpass
                    > ~/.pg_service.conf

    > TODO:
        - Define basic views
        - Models (basic for now, expand later)
        - Admin setup
        - namespace URLs
        - Generic Views

12/05/2024:
    > Daily Objective:
        - Models (basic for now, expand later)
        - Admin setup
        - Define basic views
        - Templates
        - Namespace URLs
        - Generic Views
    > Progress:
        - Models (basic for now, expand later)
            > Import User model from {django.contrib.auth.models}
            > Set up basic models for Deck, Card, Deck2Cards
                - fields, __str__, get_info, admin display
                - Will worry about additional methods later
            > Activate models in settings
                - add OptcgConfig to INSTALLED_APPS
                - $pm makemigrations optcg // $pm migrate
        - Admin setup
            > $pm createsuperuser
            > register models in ~optcg/admin.py
        - Define basic views
            > Mapped out pages that users will see + components
            ~ optcg/views.py, optcg/urls.py
        - Templates
            > Set up Templates folder
            > Set up basic templates for existing views
            > Update optcg/views.py to use templates
                - set context
                - render(request, url, context)
            > Anticipate 404 errors
                - get_object_or_404()
                **** not implemented bc no need yet ****
        - Nnamespace URLs
            > update urls.py to include app_name
            > add link to cards/decks html to link to each other
        - Generic Views
        **** Want to look into Generic Views more ****
            >CardView, DeckView            
                - amend optcg/urls.py
                - amend optcg/views.py
    > TODO:
        - Populate database via CSV
            LATER : download CSV from tcgcsv
        - Set up automated testing
        - customize admin
        - django debug toolbar