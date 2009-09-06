from django.db import models

from history.models import HistoricalRecords

class Teacher(models.Model):
	"""A teacher instructs students in lectures"""

	name = models.CharField(max_length=32)

	history = HistoricalRecords()

	def __unicode__(self):
		return u"%s" % self.name

class Lecture(models.Model):
	"""A lecture is done by a teacher""" 

	name = models.CharField(max_length=256)
	teacher = models.ForeignKey(Teacher)

	history = HistoricalRecords()

	def __unicode__(self):
		return u"%s with teacher %s" % (self.name, self.teacher)

class Student(models.Model):
	"""A student can attend just one lecture."""

	name = models.CharField(max_length=32)
	birthdate = models.DateField(null=True, blank=True)
	lecture = models.ForeignKey(Lecture, null=True)

	history = HistoricalRecords()

	def __unicode__(self):
		return u"%s attending lecture %s" % (self.name, self.lecture)

