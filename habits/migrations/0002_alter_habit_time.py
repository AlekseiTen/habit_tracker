# Generated by Django 5.0.10 on 2024-12-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("habits", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="time",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Время"),
        ),
    ]