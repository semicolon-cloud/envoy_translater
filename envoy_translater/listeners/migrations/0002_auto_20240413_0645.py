# Generated by Django 3.2.25 on 2024-04-13 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('listeners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='route',
            name='updated_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]