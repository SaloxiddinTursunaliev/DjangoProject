# Generated by Django 4.0 on 2021-12-27 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0008_choice_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='pub_date',
        ),
    ]
