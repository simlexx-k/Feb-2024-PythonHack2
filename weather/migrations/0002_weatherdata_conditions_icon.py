# Generated by Django 5.0.4 on 2024-04-26 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherdata',
            name='conditions_icon',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
