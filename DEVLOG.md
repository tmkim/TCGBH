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

12/06/2024:
    > Daily Objective:
        - Populate database via CSV
        - django debug toolbar
        - customize admin
        - Set up automated testing
        - 
    > Progress:
        - Populate database via CSV
            > new tools folder
                ~ csv.json  csv2json.py  test.csv
            > pm loaddata {fixture}.json 
                .. This is good for one-time import
            LATER : figure out how to do automatically
            LATER : learn more about Fixtures

        - Django Debug Toolbar (https://django-debug-toolbar.readthedocs.io/en/latest/installation.html)
            > python -m pip install django-debug-toolbar
            > update bountyhunter/settings.py
                (INSTALLED_APPS, MIDDLEWARE, DEBUG_TOOLBAR_CONFIG)
            > update bountyhunter/urls.py
                path('__debug__/', include('debug_toolbar.urls'))
            ** Only appears on admin **

        - customize admin
            > updae optcg/admin.py
            > include @admin.display in optcg/models.py
            ** more admin customization : https://docs.djangoproject.com/en/5.1/intro/tutorial07/

        - Set up automated testing
            > optcg/tests.py
            > pm test --keepdb optcg
                .. don't need "--keepdb" but helps with issues re: permissions to create/delete db
                .. having some issues with user having permission to create db
                .. hotfix -> 
                    - update settings.py to set TEST db name
                    $ sudo -u postgres psql postgres
                    > CREATEDB test_db;
            LATER : add more tests, tests for views

    > TODO:
        - LATER : Set up test for views
        - Start building individual card lookup

12/20/2024
    > Daily Objective:
        - Implement Django Rest Framework
    > Progress:
        - Implement Django Rest Framework
            > set up new app api_optcg
            > update models.py
            > create serializers.py (use HyperlinkedModelSerializer)
                .. not sure if Hyperlink necessary yet, can change later
            > generic viewsets for deck, cards, users, api_root
                .. need deck2cards
            > update project urls.py to include new app
            > update app urls.py to use router for API endpoints
            > tested that data can be added to and retrieved from database

    > TODO:
        - Flesh out relations/hyperlinks
            - Auth & Permissions
            - Req & Response

1/7/2025
    Just popping in to include the idea of implementing pyspark for maintaining the database using CSVs from tcgcsv. Good for processing large files and scheduling batch jobs - could be a great option for daily updates for market prices.