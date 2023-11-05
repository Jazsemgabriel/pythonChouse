# Generated by Django 4.2.7 on 2023-11-05 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_alter_contacto_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
        migrations.AddField(
            model_name='contacto',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
