# Generated by Django 4.2.6 on 2023-11-02 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshorter', '0005_shortyurl_updated_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortyurl',
            name='timstamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]