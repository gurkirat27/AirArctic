# Generated by Django 3.2.25 on 2024-10-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='price',
            field=models.DecimalField(decimal_places=2, default=250, max_digits=5),
        ),
    ]
