# Generated by Django 4.2.7 on 2023-12-14 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetest', '0002_rename_women_persons'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]