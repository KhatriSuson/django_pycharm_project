# Generated by Django 4.2.2 on 2023-06-19 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sn', models.IntegerField(primary_key=1, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=150)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=140)),
            ],
        ),
    ]
