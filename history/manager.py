from django.db import models
from django.db.models.fields.related import RelatedField

import copy 
from history import related
#from history.descriptor import HistoricalObjectDescriptor

class HistoryDescriptor(object):
    def __init__(self, model):
        self.model = model

    def __get__(self, instance, owner):
        if instance is None:
            return HistoryManager(self.model)
        return HistoryManager(self.model, instance)

class HistoryManager(models.Manager):
    def __init__(self, model, instance=None):
        super(HistoryManager, self).__init__()
        self.model = model
        self.instance = instance

    def get_query_set(self):
        if self.instance is None:
            return super(HistoryManager, self).get_query_set()

        filter = {self.instance._meta.pk.name: self.instance.pk}
        return super(HistoryManager, self).get_query_set().filter(**filter)

    def most_recent(self):
        """
        Returns the most recent copy of the instance available in the history.
        """
        if not self.instance:
            raise TypeError("most_recent() is accessible only via history of %s instances " % \
                            self.model._meta.object_name)
        fields = (field.name for field in self.instance._meta.fields)
        try:
            values = self.values_list(*fields)[0]
        except IndexError:
            raise self.instance.DoesNotExist("%s has no historical record." % \
                                             self.instance._meta.object_name)
        #TBD LF: check for "-" as in as_of ??!
        return self.instance.__class__(*values)

    def as_of(self, date):
        """
        Returns an instance of the original model with all the attributes set
        according to what was present on the object on the date provided.
        """
        if not self.instance:
            raise TypeError("as_of() is accessible only via history of %s instances " % \
                            self.model._meta.object_name)
        fields = (field.name for field in self.instance._meta.fields)
        qs = self.filter(history_date__lte=date)
        try:
            values = qs.values_list('history_type', *fields)[0]
        except IndexError:
            raise self.instance.DoesNotExist("%s had not yet been created." % \
                                             self.instance._meta.object_name)
        if values[0] == '-':
            raise self.instance.DoesNotExist("%s had already been deleted." % \
                                             self.instance._meta.object_name)
        return self.create_instance(date, *values[1:])

    def create_instance(self, date, *instance_values):
        """Instantiate class with special attributes needed to follow external
        relations in time-aware fashion
   
        :param date: as_of date
        :type date: date or datetime instance

        :param *instance_values: each arg needed to instantiate a new instance.__class__
        :type instance_values: list of values

        """
        time_aware_model = self.create_instance_model(self.instance.__class__)

        found_instance = time_aware_model(*instance_values)
        found_instance._as_of = date
        return found_instance
        
    def create_instance_model(self, model):
        """
        Creates time-aware model class to associate with the instance retrieved.
        This class updates fields replacing related accessors with time-aware accessors.
        """
       
        if getattr(model, '_historical_model', False):
            # Historical transformation has already been applied
            return model

        attrs = self.copy_fields(model)
        # This is needed to do not apply historical transformation twice
        attrs['_historical_model'] = True
        attrs['history_object'] = HistoricalObjectDescriptor(model),
        attrs['__unicode__'] = lambda self: u"%s" % self.history_object

        name = "Actual%s" % model._meta.object_name
        return type(name, (models.Model,), attrs)

    def copy_fields(self, model):
        print "HistoryManager.copy_fields from %s" % model.__name__
        """
        Creates copies of the model's original fields, returning
        a dictionary mapping field name to copied field object.
        """
        # Though not strictly a field, this attribute
        # is required for a model to function properly.
        fields = {'__module__': model.__module__}

        for field in model._meta.fields:

            # Update only related fields 

            field = copy.copy(field)

            if isinstance(field, RelatedField):

                field.__class__ = related.HistoricalForeignKey

            fields[field.name] = field

        return fields

