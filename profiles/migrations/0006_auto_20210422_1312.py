# Generated by Django 3.1.6 on 2021-04-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20210407_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceuser',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='serviceuser',
            name='lastname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200),
        ),
    ]