# Generated by Django 4.1.7 on 2023-03-08 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='age',
            field=models.PositiveIntegerField(verbose_name='возраст'),
        ),
    ]
