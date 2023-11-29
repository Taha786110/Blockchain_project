# Generated by Django 4.2.6 on 2023-11-20 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="details_csv",
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
                ("verify_id", models.CharField(blank=True, max_length=12)),
                ("name", models.CharField(blank=True, max_length=122)),
                ("program", models.CharField(blank=True, max_length=122)),
                ("year", models.CharField(blank=True, max_length=8)),
                ("tx_rc", models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
