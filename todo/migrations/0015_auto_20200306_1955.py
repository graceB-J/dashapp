# Generated by Django 3.0.2 on 2020-03-07 00:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_auto_20200306_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2020, 3, 6, 19, 55, 3, 53532)),
        ),
    ]
