# Generated by Django 2.1.3 on 2019-01-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jstore', '0012_auto_20190123_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='highscores',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gamesave',
            name='gamestate',
            field=models.CharField(default='', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='gamesave',
            name='scores',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
