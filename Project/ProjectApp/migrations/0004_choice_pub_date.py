# Generated by Django 4.0 on 2021-12-27 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0003_remove_choice_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
    ]