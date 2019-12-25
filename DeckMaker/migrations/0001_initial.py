# Generated by Django 2.2.7 on 2019-12-22 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeckId', models.IntegerField()),
                ('DeckName', models.CharField(max_length=75)),
                ('DeckOwner', models.CharField(max_length=30)),
                ('DeckDate', models.DateField()),
            ],
            options={
                'db_table': 'Decks',
            },
        ),
    ]