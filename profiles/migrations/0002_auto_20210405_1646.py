# Generated by Django 3.1.6 on 2021-04-05 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='serviceprovider',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='serviceuser',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='serviceuser',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='endtime',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='meetdate',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='meetplace',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='starttime',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='availability',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='service',
            field=models.CharField(choices=[('Personal Support Assistance', 'Personal Support Assistance'), ('Ugandan Sign Language Interpreter', 'Ugandan Sign Language Interpreter'), ('International Sign Language Interpreter', 'International Sign Language Interpreter'), ('Captioning', 'Captioning'), ('Mobility Guide', 'Mobility Guide')], max_length=200, null=True),
        ),
    ]
