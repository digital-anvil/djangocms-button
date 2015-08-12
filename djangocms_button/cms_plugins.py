from __future__ import unicode_literals

import django

from django.contrib.sites.models import Site
from django.conf import settings
from django.template.loader import select_template
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .forms import ButtonForm
from .models import Button


class ButtonPlugin(CMSPluginBase):
    name = _('Button Link')
    module = settings.DJANGOCMS_BUTTON_MODULE
    model = Button
    form = ButtonForm
    text_enabled = settings.DJANGOCMS_BUTTON_TEXT_ENABLED
    allow_children = True
    child_classes = settings.DJANGOCMS_BUTTON_CHILD_CLASSES
    TEMPLATE_PATH = 'djangocms_button/{template}.html'
    render_template = TEMPLATE_PATH.format(template=settings.DJANGOCMS_BUTTON_DEFAULT_TEMPLATE)

    def render(self, context, instance, placeholder):
        template = select_template((
            self.TEMPLATE_PATH.format(template=instance.template),
            self.TEMPLATE_PATH.format(template=settings.DJANGOCMS_BUTTON_DEFAULT_TEMPLATE),
        ))

        if django.VERSION[1] >= 8:
            self.render_template = template.template
        else:
            self.render_template = template

        link = instance.link()
        context.update({
            'name': instance.name,
            'link': link,
            'target': instance.target,
            'placeholder': placeholder,
            'object': instance
        })
        return context

    def get_form(self, request, obj=None, **kwargs):
        form_class = super(ButtonPlugin, self).get_form(request, obj, **kwargs)

        if obj and obj.page and obj.page.site:
            site = obj.page.site
        elif self.page and self.page.site:
            site = self.page.site
        else:
            site = Site.objects.get_current()

        class Form(form_class):
            def __init__(self, *args, **kwargs):
                super(Form, self).__init__(*args, **kwargs)
                self.for_site(site)

        return Form

    def icon_src(self, instance):
        return settings.STATIC_URL + u'cms/img/icons/plugins/link.png'

plugin_pool.register_plugin(ButtonPlugin)
