# Generated by Django 4.2 on 2023-12-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="offer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item", models.CharField(max_length=30)),
                ("desc", models.TextField()),
                ("icon", models.CharField(max_length=100)),
            ],
        ),
    ]