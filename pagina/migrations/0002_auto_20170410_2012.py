# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publishe_date',
            new_name='published_date',
        ),
    ]
