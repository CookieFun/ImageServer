# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myphoto',
            name='owner',
        ),
        migrations.AddField(
            model_name='myphoto',
            name='name',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
