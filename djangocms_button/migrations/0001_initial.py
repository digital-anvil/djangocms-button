# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Button',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('url', models.CharField(max_length=2048, null=True, verbose_name='link', blank=True)),
                ('anchor', models.CharField(help_text='This applies only to page and text links. Do <em>not</em> include a preceding "#" symbol.', max_length=128, verbose_name='anchor', blank=True)),
                ('mailto', models.EmailField(help_text='An email address has priority over a text link.', max_length=75, null=True, verbose_name='email address', blank=True)),
                ('phone', models.CharField(help_text='A phone number has priority over a mailto link.', max_length=40, null=True, verbose_name='Phone', blank=True)),
                ('target', models.CharField(blank=True, max_length=100, verbose_name='target', choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')])),
                ('template', models.CharField(default=b'default', max_length=255, verbose_name='template', choices=[(b'default', 'Default')])),
                ('page_link', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='cms.Page', help_text='A link to a page has priority over a text link.', null=True, verbose_name='page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
