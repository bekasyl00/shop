# Generated by Django 4.2.2 on 2023-09-05 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_order_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='time',
            new_name='timer',
        ),
    ]
