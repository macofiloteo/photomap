# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import photomap.models


class Migration(migrations.Migration):

    dependencies = [
        ('photomap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagespot',
            name='image',
            field=models.ImageField(default=b'/static/photomap/img/zambologo.jpeg', upload_to=photomap.models.upload_to),
        ),
    ]
