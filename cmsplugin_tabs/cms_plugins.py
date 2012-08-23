from django.contrib import admin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugin_tabs.models import TabHeaderPlugin, TabTitle

class TabTitleInline(admin.StackedInline):
    model = TabTitle

class CMSTabHeaderPlugin(CMSPluginBase):
    model = TabHeaderPlugin
    name = "Tabs Header"
    inlines = [TabTitleInline]
    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context.update({
            'tabheader_instance': instance,
            'header_id': "{}-header".format(instance.id),
            'content_id': "{}-content".format(instance.id),
        })
        request = context['request']
        request.tabheader = instance
        return context
plugin_pool.register_plugin(CMSTabHeaderPlugin)
