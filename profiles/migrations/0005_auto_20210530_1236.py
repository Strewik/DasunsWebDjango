# Generated by Django 3.1.6 on 2021-05-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20210524_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='endtime',
            field=models.TimeField(max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='meetdate',
            field=models.DateField(max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='starttime',
            field=models.TimeField(max_length=200),
        ),
    ]