# Generated by Django 3.1.3 on 2020-12-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=254)),
            ],
        ),
    ]
