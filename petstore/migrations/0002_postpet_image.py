# Generated by Django 3.1.1 on 2020-09-04 12:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('petstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpet',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]