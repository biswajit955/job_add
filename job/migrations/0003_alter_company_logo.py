# Generated by Django 4.0 on 2022-05-06 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_alter_post_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.FileField(upload_to='media/'),
        ),
    ]
