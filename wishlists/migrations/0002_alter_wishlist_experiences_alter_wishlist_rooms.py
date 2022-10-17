# Generated by Django 4.1.1 on 2022-09-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiences", "0002_experience_category_alter_perk_details_and_more"),
        ("rooms", "0004_room_category"),
        ("wishlists", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="experiences",
            field=models.ManyToManyField(blank=True, to="experiences.experience"),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="rooms",
            field=models.ManyToManyField(blank=True, to="rooms.room"),
        ),
    ]
