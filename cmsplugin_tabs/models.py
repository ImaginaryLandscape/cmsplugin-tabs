from django.db import models
from cms.models import CMSPlugin
from cmsplugin_tabs import utils

TEMPLATE_CHOICES = utils.autodiscover_templates()

class TabHeaderPlugin(CMSPlugin):
    template = models.CharField(max_length=128, choices=TEMPLATE_CHOICES)
    tab_count = models.IntegerField()

    def __unicode__(self):
        return u"{}".format(self.tab_count)

class TabTitle(models.Model):
    title = models.CharField(max_length=64)
    tab_header = models.ForeignKey(TabHeaderPlugin)
