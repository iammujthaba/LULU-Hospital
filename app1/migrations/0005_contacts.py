# Generated by Django 3.2.18 on 2023-05-10 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_booking_booked_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('y_name', models.CharField(max_length=100)),
                ('y_phone', models.CharField(max_length=10)),
                ('y_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
