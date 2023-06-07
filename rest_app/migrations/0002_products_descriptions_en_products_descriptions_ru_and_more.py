# Generated by Django 4.2.1 on 2023-06-05 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='descriptions_en',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='products',
            name='descriptions_ru',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='products',
            name='gender_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='products',
            name='gender_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='products',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='products',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Name'),
        ),
    ]
