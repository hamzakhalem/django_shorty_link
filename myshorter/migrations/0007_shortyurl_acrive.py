# Generated by Django 4.2.6 on 2023-11-04 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshorter', '0006_shortyurl_timstamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortyurl',
            name='acrive',
            field=models.BooleanField(default=True),
        ),
    ]
