# Generated by Django 3.1.6 on 2021-04-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_auto_20210428_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
