# Generated by Django 2.2.2 on 2019-10-05 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_te'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='te',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]