# Generated by Django 3.0.2 on 2020-03-07 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades', '0009_auto_20200306_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='grade_percentage',
        ),
    ]
