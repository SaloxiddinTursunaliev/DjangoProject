# Generated by Django 4.0 on 2021-12-27 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
