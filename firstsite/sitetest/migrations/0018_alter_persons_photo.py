# Generated by Django 4.2.7 on 2024-02-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitetest', '0017_filemodel_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persons',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo'),
        ),
    ]