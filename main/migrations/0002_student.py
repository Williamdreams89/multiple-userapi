# Generated by Django 4.1.1 on 2022-09-21 12:27

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('main.user',),
            managers=[
                ('student', django.db.models.manager.Manager()),
            ],
        ),
    ]