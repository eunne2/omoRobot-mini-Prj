# Generated by Django 4.1.5 on 2023-01-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="info", name="a", field=models.IntegerField(default=0),
        ),
    ]
