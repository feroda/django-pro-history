from django.core.management.base import BaseCommand, NoArgsCommand, CommandError
from optparse import make_option
import os, sys, types, re

from school.models import *
import datetime

def init_data():
	"""Initialize some data"""
	t1 = Teacher(name="Renzo Davoli")
	t1.save()
	t2 = Teacher(name="Claudio Baglioni")
	t2.save()
	l1 = Lecture(name="Operating Systems", teacher=t1)
	l1.save()
	l2 = Lecture(name="Virtual insanity", teacher=t1)
	l2.save()
	l3 = Lecture(name="Singing 'Piccolo grande amore'", teacher=t2)
	l3.save()
	l4 = Lecture(name="Playing 'Piccolo grande amore'", teacher=t2)
	l4.save()
	p1 = Student(name="Luca Ferroni", birthdate=datetime.date(1980,2,17), lecture=l1)
	p1.save()
	p2 = Student(name="Mario Rossi", birthdate=datetime.date(1979,1,1), lecture=l3)
	p2.save()
	p3 = Student(name="Franco Verdi", birthdate=datetime.date(1954,1,1), lecture=l1)
	p3.save()
	p4 = Student(name="Tommaso Bianchi", birthdate=datetime.date(1954,1,1), lecture=l3)
	p4.save()

def main():

	print("""A long time ago in a far away galaxy ... \
	""")

	# Initialize some data
	teachers = Teacher.objects.all()
	students = Student.objects.all()
	lectures = Lecture.objects.all()
	if not (teachers.count() or students.count() or lectures.count()):
		init_data()

	print("The situation is...")
	for s in students:
	  print("%s with teacher %s" % (s, s.lecture.teacher))

class Command(NoArgsCommand):
	help = "Initialize school demo application"
	args = ''

	option_list = BaseCommand.option_list 

	def handle(self, ws='', *args, **options):
		main()


