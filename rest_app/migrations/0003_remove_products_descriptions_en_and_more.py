# Generated by Django 4.2.2 on 2023-06-06 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0002_products_descriptions_en_products_descriptions_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='descriptions_en',
        ),
        migrations.RemoveField(
            model_name='products',
            name='descriptions_ru',
        ),
        migrations.RemoveField(
            model_name='products',
            name='gender_en',
        ),
        migrations.RemoveField(
            model_name='products',
            name='gender_ru',
        ),
        migrations.RemoveField(
            model_name='products',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='products',
            name='name_ru',
        ),
    ]
