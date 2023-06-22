# Generated by Django 4.2.2 on 2023-06-22 11:43

import MyPlant_App_remake_exam.my_web.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2, message='It should consist of a minimum of 2 characters!'), MyPlant_App_remake_exam.my_web.models.validate_plant_name])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2, message='It should consist of a minimum of 2 characters!')])),
                ('first_name', models.CharField(max_length=20, validators=[MyPlant_App_remake_exam.my_web.models.validate_first_name])),
                ('last_name', models.CharField(max_length=20, validators=[MyPlant_App_remake_exam.my_web.models.validate_first_name])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]