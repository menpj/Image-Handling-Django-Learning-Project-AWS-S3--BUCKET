# Generated by Django 5.1.6 on 2025-02-28 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageuploadapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='image',
            field=models.FileField(upload_to='dogs/'),
        ),
    ]
