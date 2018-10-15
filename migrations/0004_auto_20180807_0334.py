# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photomap', '0003_auto_20180807_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagespot',
            old_name='layer_name_link',
            new_name='establishment_type',
        ),
        migrations.AddField(
            model_name='imagespot',
            name='name',
            field=models.CharField(default=datetime.datetime(2018, 8, 7, 3, 34, 26, 329228, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]
