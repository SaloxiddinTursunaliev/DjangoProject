# Generated by Django 4.0 on 2021-12-27 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0004_choice_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='pub_date',
        ),
    ]