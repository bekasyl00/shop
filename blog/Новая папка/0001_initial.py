# Generated by Django 4.2.2 on 2023-06-09 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(verbose_name='Уникальная названия')),
                ('title', models.CharField(max_length=200, verbose_name='Нозвания товара')),
                ('image', models.CharField(max_length=200, verbose_name='Фото товара')),
                ('desc', models.TextField(verbose_name='Описания товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
            ],
        ),
    ]
