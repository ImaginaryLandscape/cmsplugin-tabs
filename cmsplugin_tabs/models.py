from django.db import models
from cms.models import CMSPlugin
from cmsplugin_tabs import utils

TEMPLATE_CHOICES = utils.autodiscover_templates()

class TabHeaderPlugin(CMSPlugin):
    template = models.CharField(max_length=128, choices=TEMPLATE_CHOICES)
    tab_count = models.IntegerField()

    def copy_relations(self, oldinstance):
        for associated_item in oldinstance.tabtitle_set.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            associated_item.pk = None
            associated_item.tab_header = self
            associated_item.save()

    def __unicode__(self):
        return u"{}".format(self.tab_count)

class TabTitle(models.Model):
    title = models.CharField(max_length=64)
    tab_header = models.ForeignKey(TabHeaderPlugin)
