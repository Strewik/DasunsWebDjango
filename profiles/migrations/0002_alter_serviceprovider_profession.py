# Generated by Django 3.2.3 on 2021-10-25 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='profession',
            field=models.CharField(max_length=10000),
        ),
    ]