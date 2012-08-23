from cmsplugin_tabs.models import TabHeaderPlugin

def tabs_plugin_processor(instance, placeholder, rendered_content, original_context):
    request = original_context['request']
    if isinstance(instance, TabHeaderPlugin):
        request.tab_count = instance.tab_count
        request.tab_header = instance
        return '{}\n<div class="tab-content">'.format(rendered_content)
    else:
        todo = getattr(request, 'tab_count', 0)
        if todo:
            tab_header = request.tab_header
            request.tab_count -= 1
            retval = '<div class="tab-pane" id="tab-{}-{}">\n{}\n</div>'.format(
                tab_header.id, tab_header.tab_count - request.tab_count,
                rendered_content)
            if request.tab_count == 0 or original_context['plugin']['last']:
                retval = "{}\n</div>".format(retval)
            return retval
    return rendered_content