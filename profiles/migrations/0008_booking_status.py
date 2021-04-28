# Generated by Django 3.1.6 on 2021-04-28 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_merge_20210426_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Booked', 'Booked'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], max_length=200, null=True),
        ),
    ]