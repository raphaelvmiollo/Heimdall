# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=70)),
                ('host_ftp', models.CharField(max_length=50)),
                ('pass_ftp', models.CharField(max_length=50)),
                ('user_ftp', models.CharField(max_length=50)),
                ('name_db', models.CharField(max_length=50)),
                ('host_db', models.CharField(max_length=50)),
                ('user_db', models.CharField(max_length=50)),
                ('pass_db', models.CharField(max_length=50)),
                ('prefix_db', models.CharField(max_length=30)),
            ],
        ),
    ]
