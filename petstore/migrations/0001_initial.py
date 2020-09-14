# Generated by Django 3.1.1 on 2020-09-04 09:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostPet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet', models.CharField(max_length=50)),
                ('pet_name', models.CharField(max_length=50)),
                ('pet_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Unspecified')], max_length=1)),
                ('pet_breed', models.CharField(max_length=50)),
                ('pet_color', models.CharField(max_length=50)),
                ('pet_detail', models.TextField(max_length=500)),
                ('pet_DOB', models.DateField()),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]