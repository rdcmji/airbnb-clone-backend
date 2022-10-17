# Generated by Django 4.1.1 on 2022-10-01 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0006_alter_room_amenities_alter_room_category"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "experiences",
            "0003_alter_experience_category_alter_experience_host_and_more",
        ),
        ("wishlists", "0002_alter_wishlist_experiences_alter_wishlist_rooms"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="experiences",
            field=models.ManyToManyField(
                blank=True, related_name="wishlists", to="experiences.experience"
            ),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="rooms",
            field=models.ManyToManyField(
                blank=True, related_name="wishlists", to="rooms.room"
            ),
        ),
        migrations.AlterField(
            model_name="wishlist",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wishlists",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
