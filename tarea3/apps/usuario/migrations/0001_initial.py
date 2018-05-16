# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('eMail', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=16)),
                ('password2', models.CharField(max_length=16)),
            ],
        ),
    ]
