# Generated by Django 4.2.7 on 2023-12-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_reservation_no_guest_alter_reservation_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='table_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='table',
            name='number_table',
            field=models.CharField(max_length=150),
        ),
    ]
