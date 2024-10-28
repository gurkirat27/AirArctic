# Generated by Django 3.2.25 on 2024-10-23 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0007_carddetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingReferenceNumber', models.CharField(max_length=10)),
                ('isMember', models.BooleanField(default=False)),
                ('contactEmail', models.EmailField(max_length=254)),
                ('passanger', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Trip.passengers')),
                ('payment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Trip.carddetails')),
                ('trip', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='Trip.trip')),
            ],
        ),
    ]
