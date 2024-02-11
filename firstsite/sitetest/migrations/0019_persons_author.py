# Generated by Django 4.2.7 on 2024-02-11 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitetest', '0018_alter_persons_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='persons',
            name='author',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]