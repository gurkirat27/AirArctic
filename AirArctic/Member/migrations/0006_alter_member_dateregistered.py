# Generated by Django 3.2.25 on 2024-11-20 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0005_alter_memberdetails_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='dateRegistered',
            field=models.DateField(auto_now=True),
        ),
    ]