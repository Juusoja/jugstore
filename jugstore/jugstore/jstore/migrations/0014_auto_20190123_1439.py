# Generated by Django 2.1.3 on 2019-01-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jstore', '0013_auto_20190123_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='highscores',
            field=models.CharField(default=[], max_length=100),
        ),
    ]