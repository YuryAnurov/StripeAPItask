# Generated by Django 4.1.4 on 2023-02-20 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('subid', models.IntegerField(default=-1, primary_key=True, serialize=False)),
                ('name', models.CharField(default='Complex Order', max_length=20)),
                ('description', models.TextField(default='заказик')),
                ('price', models.DecimalField(decimal_places=2, default=100500, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('counter', models.IntegerField(default=0)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase.order')),
            ],
        ),
    ]
