# Generated by Django 4.2.13 on 2024-07-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saving', '0003_alter_profile_nominated_bank_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
