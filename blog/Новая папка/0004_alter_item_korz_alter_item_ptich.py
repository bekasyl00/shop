# Generated by Django 4.2.2 on 2023-08-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_item_korz_item_ptich'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='korz',
            field=models.ImageField(default='public/public/img/10354898_cart_trolley_ui_web_icon.svg', upload_to='items'),
        ),
        migrations.AlterField(
            model_name='item',
            name='ptich',
            field=models.ImageField(default='public/public/img/326572_check_icon.svg', upload_to='items'),
        ),
    ]
