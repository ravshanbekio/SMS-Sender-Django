# Generated by Django 4.0.3 on 2022-03-27 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]
