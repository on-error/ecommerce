# Generated by Django 3.1.3 on 2020-11-21 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.IntegerField()),
                ('address', models.CharField(max_length=700)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=10)),
            ],
        ),
    ]