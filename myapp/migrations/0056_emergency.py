# Generated by Django 4.2.7 on 2023-12-02 15:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0055_criminalprofile_criminal_detail_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="EMERGENCY",
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
                ("timestamp", models.TimeField(default=django.utils.timezone.now)),
                ("emergency_location", models.ManyToManyField(to="myapp.mapmarker")),
                (
                    "sender",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="myapp.userprofile",
                    ),
                ),
            ],
        ),
    ]
