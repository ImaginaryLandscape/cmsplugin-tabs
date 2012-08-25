from cmsplugin_tabs.models import TabHeaderPlugin
from django.template.loader import find_template

def tabs_plugin_processor(instance, placeholder, rendered_content, original_context):
    request = original_context['request']
    if isinstance(instance, TabHeaderPlugin):
        wrap_info = {
            'wrapper_plugin': instance,
            'context': original_context,
            'plugins': [],
            'plugin_counter': instance.tab_count,
            }
        request.wrap_info = wrap_info
    else:
        wrap_info = getattr(request, 'wrap_info', None)
        todo = wrap_info and wrap_info['plugin_counter']
        if todo and not(instance._render_meta.text_enabled and instance.parent):
            wrap_info['plugin_counter'] -= 1
            wrap_info['plugins'].append(rendered_content)
            if wrap_info['plugin_counter'] == 0 or original_context['plugin']['last']:
                wrapper_plugin = wrap_info['wrapper_plugin']
                template = find_template(wrapper_plugin.template)[0]
                context = wrap_info['context']
                context['plugins'] = wrap_info['plugins']
                request.wrap_info = None
                return template.render(context)
        else:
            # we're not in a wrapper, just return what we got untouched
            return rendered_content
    return u""
