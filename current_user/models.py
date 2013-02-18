from django.db import models
from django.contrib.auth.models import User

from current_user import registration

class CurrentUserField(models.ForeignKey):
    def __init__(self, **kwargs):
        # Kwargs always rewritten needed to use in South migrations
        kwargs['to'] = User
        kwargs['null'] = True
        super(CurrentUserField, self).__init__(**kwargs)

    def contribute_to_class(self, cls, name):
        super(CurrentUserField, self).contribute_to_class(cls, name)
        registry = registration.FieldRegistry()
        registry.add_field(cls, self)
