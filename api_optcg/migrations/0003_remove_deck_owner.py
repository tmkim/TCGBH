# Generated by Django 5.1.4 on 2024-12-20 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_optcg', '0002_rename_url_card_tcgurl_deck2cards'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='owner',
        ),
    ]
