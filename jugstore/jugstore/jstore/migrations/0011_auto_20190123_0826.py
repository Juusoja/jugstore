# Generated by Django 2.1.3 on 2019-01-23 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jstore', '0010_auto_20190122_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesave',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jstore.Game'),
        ),
        migrations.AlterField(
            model_name='gamesave',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]