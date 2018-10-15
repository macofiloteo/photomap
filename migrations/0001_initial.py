# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields
import photomap.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Baranggay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('geom', djgeojson.fields.PointField()),
            ],
        ),
        migrations.CreateModel(
            name='ImageSpot',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geom', djgeojson.fields.PointField()),
                ('description', models.TextField()),
                ('layer_name_link', models.CharField(max_length=20)),
                ('image', models.ImageField(default=b'', upload_to=photomap.models.upload_to)),
            ],
        ),
    ]
