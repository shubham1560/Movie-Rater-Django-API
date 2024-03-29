# Generated by Django 2.2.2 on 2019-10-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20191005_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rating',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
