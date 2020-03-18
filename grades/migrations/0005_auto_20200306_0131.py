# Generated by Django 3.0.2 on 2020-03-06 06:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0004_auto_20200305_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='improved',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_grade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, validators=[django.core.validators.MaxValueValidator(200), django.core.validators.MinValueValidator(0)]),
        ),
    ]
