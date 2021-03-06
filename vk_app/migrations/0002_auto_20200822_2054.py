# Generated by Django 2.2.13 on 2020-08-22 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vk_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='access',
            name='app_id',
            field=models.IntegerField(null=True, verbose_name='id приложения'),
        ),
        migrations.AddField(
            model_name='access',
            name='user_id',
            field=models.IntegerField(null=True, verbose_name='id пользователя vk'),
        ),
        migrations.AlterField(
            model_name='access',
            name='token',
            field=models.CharField(max_length=200, null=True, verbose_name='Access token'),
        ),
    ]
