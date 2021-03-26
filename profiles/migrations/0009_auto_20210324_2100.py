# Generated by Django 3.1.6 on 2021-03-24 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20210324_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceprovider',
            old_name='availability',
            new_name='sunday',
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='friday',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='monday',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='saturday',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='thursday',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='tuesday',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='wednesday',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
