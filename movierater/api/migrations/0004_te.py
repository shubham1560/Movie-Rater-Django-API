# Generated by Django 2.2.2 on 2019-09-26 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190926_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Te',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
