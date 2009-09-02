from django.db import models

from history.models import HistoricalRecords

"""Basic model to test history application developed by Marty Alchin."""

class Organization(models.Model):

	name = models.CharField(max_length=32)
	address = models.CharField(max_length=32)
	nemployers = models.PositiveIntegerField()
	
	history = HistoricalRecords()

	def __unicode__(self):
		return u"%s (%s)" % (self.name, self.nemployers)

class Person(models.Model):

	name = models.CharField(max_length=32)
	nick = models.CharField(max_length=32, null=True)
	birthdate = models.DateField(null=True, blank=True)
	nsons = models.PositiveIntegerField()
	wife = models.ForeignKey("Person", null=True)

	history = HistoricalRecords()

	def __unicode__(self):
		return u"%s `%s` (%d)" % (self.name, self.nick, self.nsons)

class OrgRole(models.Model):

	org = models.ForeignKey(Organization)
	person = models.ForeignKey(Person, related_name="roles")
	role = models.CharField(max_length=32)
	
	history = HistoricalRecords()

	def __unicode__(self):
		return u"%s in %s (%s)" % (self.person, self.org, self.role)

