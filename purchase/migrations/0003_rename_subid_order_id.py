# Generated by Django 4.1.4 on 2023-02-20 06:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0002_alter_item_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='subid',
            new_name='id',
        ),
    ]
