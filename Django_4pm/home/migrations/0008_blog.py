# Generated by Django 4.2.2 on 2023-06-22 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_feedback_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('full_body', models.TextField()),
                ('category', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=300)),
                ('date', models.DateField()),
            ],
        ),
    ]
