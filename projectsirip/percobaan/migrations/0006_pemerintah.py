# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('percobaan', '0005_auto_20170619_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='pemerintah',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instansi', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'pemerintah',
            },
        ),
    ]