# Development Log

MM/DD/YYYY:
    > Daily Objective:
        - 
    > Progress:
        - 
    > TODO:
        - 

12/4/2024:
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
                > pip install django
                > pip install postgres
                    > bountyhunter/settings.py
                    > cdt/.pg_pass -> chmod 600 .pgpass
                    > ~/.pg_service.conf

    > TODO:
        - Models (basic for now, expand later)
        - Admin setup
        - namespace URLs
        - Generic Views