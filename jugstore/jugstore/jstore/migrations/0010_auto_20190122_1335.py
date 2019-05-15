# Generated by Django 2.1.3 on 2019-01-22 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jstore', '0009_auto_20190110_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameSave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scores', models.CharField(default='', max_length=100)),
                ('gamestate', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='gameurl',
            field=models.URLField(default='http://webcourse.cs.hut.fi/example_game.html', max_length=100),
        ),
        migrations.AddField(
            model_name='gamesave',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jstore.Game'),
        ),
        migrations.AddField(
            model_name='gamesave',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
