# Generated by Django 4.2.1 on 2023-07-27 01:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("learnpython", "0002_remove_title_writer"),
    ]

    operations = [
        migrations.AddField(
            model_name="body",
            name="image1",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="body",
            name="image2",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]