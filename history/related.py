
__author__     = "Luca Ferroni <feroda@users.sourceforge.net>"

import copy 

from django.db import models
from django.db.models.fields import related

class HistoricalReverseSingleRelatedObjectDescriptor(related.ReverseSingleRelatedObjectDescriptor):

    def __get__(self, instance, instance_type=None):

        rv = super(HistoricalReverseSingleRelatedObjectDescriptor, self).__get__(instance, instance_type)
        #LF print "AAAA instance=%s, rv=%s" % (instance, rv)
        if instance and rv:
            rv = rv._default_history.as_of(instance._as_of)

        return rv

class HistoricalForeignKey(models.ForeignKey):
    """Historical Foreign Key: alter contribute_to_class method
    in order to return time-aware  manager"""

    def contribute_to_class(self, cls, name):
        rv = super(HistoricalForeignKey, self).contribute_to_class(cls, name)
        # OVERRIDE foreign key descriptor !
        #DEBUG LF: raise ValueError(self.rel.__dict__)
        delattr(cls, self.name)
        setattr(cls, self.name, HistoricalReverseSingleRelatedObjectDescriptor(self))
        return rv

    def contribute_to_related_class(self, cls, related):

        return super(HistoricalForeignKey, self).contribute_to_related_class(cls, related)

