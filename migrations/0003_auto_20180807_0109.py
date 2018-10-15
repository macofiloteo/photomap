# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photomap', '0002_auto_20180308_0122'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Baranggay',
            new_name='Barangay',
        ),
    ]
