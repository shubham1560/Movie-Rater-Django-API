# Generated by Django 2.2.2 on 2019-09-24 14:52

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='stars',
            field=models.IntegerField(default=3, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'movie')},
        ),
        migrations.AlterIndexTogether(
            name='rating',
            index_together={('user', 'movie')},
        ),
    ]
