# Generated by Django 3.2.3 on 2021-08-05 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('meetplace', models.CharField(max_length=200)),
                ('meetdate', models.DateField(max_length=200)),
                ('starttime', models.TimeField(max_length=200)),
                ('endtime', models.TimeField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(blank=True, default='Pending', max_length=200)),
            ],
            options={
                'ordering': ['-date_created', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Serviceuser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True)),
                ('profile_pic', models.ImageField(blank=True, default='profile.png', upload_to='profilepics/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created', 'firstname'],
            },
        ),
        migrations.CreateModel(
            name='Serviceprovider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('nin', models.CharField(max_length=200)),
                ('dob', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200)),
                ('phyadd', models.CharField(max_length=200)),
                ('yearexp', models.CharField(max_length=200)),
                ('notmidman', models.CharField(max_length=200)),
                ('skillset', models.CharField(max_length=200)),
                ('internet', models.CharField(max_length=200)),
                ('qualification', models.FileField(blank=True, null=True, upload_to='')),
                ('portifolio', models.CharField(blank=True, max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('ref1name', models.CharField(max_length=200)),
                ('ref1title', models.CharField(max_length=200)),
                ('ref1email', models.EmailField(max_length=200)),
                ('ref1phone', models.CharField(max_length=200)),
                ('ref2name', models.CharField(max_length=200)),
                ('ref2title', models.CharField(max_length=200)),
                ('ref2email', models.EmailField(max_length=200)),
                ('ref2phone', models.CharField(max_length=200)),
                ('service', models.CharField(choices=[('Personal Support Assistance', 'Personal Support Assistance'), ('Ugandan Sign Language Interpreter', 'Ugandan Sign Language Interpreter'), ('International Sign Language Interpreter', 'International Sign Language Interpreter'), ('Captioning', 'Captioning'), ('Mobility Guide', 'Mobility Guide'), ('Tactile Sign Language Interpreter', 'Tactile Sign Language Interpreter')], max_length=200, null=True)),
                ('availability', multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=200, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Active', 'Active'), ('Suspended', 'Suspended')], max_length=200)),
                ('starttime', models.TimeField(max_length=200)),
                ('endtime', models.TimeField(max_length=200)),
                ('pricevisit', models.CharField(max_length=200)),
                ('terms', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created', 'fullname'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star', models.IntegerField(blank=True)),
                ('comment', models.CharField(blank=True, max_length=256)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.booking')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='serviceprovider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.serviceprovider'),
        ),
        migrations.AddField(
            model_name='booking',
            name='serviceuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.serviceuser'),
        ),
    ]
