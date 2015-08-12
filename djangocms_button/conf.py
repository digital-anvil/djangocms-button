# -*- coding: utf-8 -*-

from django.conf import settings  # noqa
from django.utils.translation import ugettext_lazy as _

from appconf import AppConf


class OwlConf(AppConf):
    MODULE = _('Generic')

    DEFAULT_TEMPLATE = 'default'

    CHILD_CLASSES = ()

    TEMPLATES = (
        (DEFAULT_TEMPLATE, _('Default')),
    )

    TEXT_ENABLED = True

    class Meta:
        prefix = 'djangocms_button'
