# Generated by Django 3.2.5 on 2021-08-27 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='likeDado',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='likeRecibido',
            field=models.IntegerField(null=True),
        ),
    ]
