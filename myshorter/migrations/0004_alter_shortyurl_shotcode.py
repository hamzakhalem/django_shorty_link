# Generated by Django 4.2.6 on 2023-11-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshorter', '0003_alter_shortyurl_shotcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortyurl',
            name='shotcode',
            field=models.CharField(default='mz', max_length=15, unique=True),
            preserve_default=False,
        ),
    ]
