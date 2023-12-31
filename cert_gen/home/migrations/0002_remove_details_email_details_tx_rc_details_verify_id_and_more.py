# Generated by Django 4.2.6 on 2023-11-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="details",
            name="email",
        ),
        migrations.AddField(
            model_name="details",
            name="tx_rc",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="details",
            name="verify_id",
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name="details",
            name="year",
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name="details",
            name="name",
            field=models.CharField(blank=True, max_length=122),
        ),
        migrations.AlterField(
            model_name="details",
            name="program",
            field=models.CharField(blank=True, max_length=122),
        ),
    ]
