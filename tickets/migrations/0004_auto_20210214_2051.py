# Generated by Django 3.1.6 on 2021-02-14 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20210213_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', editable=False),
        ),
    ]
