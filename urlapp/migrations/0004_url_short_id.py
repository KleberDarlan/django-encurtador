# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('urlapp', '0003_auto_20160727_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='short_id',
            field=models.UUIDField(default=uuid.uuid1, editable=False),
        ),
    ]
