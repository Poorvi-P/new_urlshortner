# Generated by Django 5.0.6 on 2024-06-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='uuid',
            field=models.CharField(max_length=5),
        ),
    ]
