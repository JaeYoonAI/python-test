# Generated by Django 4.2.5 on 2023-09-11 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.TextField(blank=True, null=True),
        ),
    ]
