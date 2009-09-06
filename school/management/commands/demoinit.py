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
	t3 = Teacher(name="Jamiroquai")
	t3.save()
	l1 = Lecture(name="Operating Systems")
	l1.save()
	l2 = Lecture(name="Virtual insanity")
	l2.save()
	l3 = Lecture(name="Singing 'Piccolo grande amore'")
	l3.save()
	l4 = Lecture(name="Playing 'Piccolo grande amore'")
	l4.save()

	# Set object insertion to 1970-01-01
	for h in Teacher.history.all():
		h.history_date = datetime.date(1970,1,1)

	for h in Lecture.history.all():
		h.history_date = datetime.date(1970,1,1)

	p1 = Student(name="Luca Ferroni", birthdate=datetime.date(1980,2,17))
	p1.save()
	p2 = Student(name="Mario Rossi", birthdate=datetime.date(1979,1,1))
	p2.save()
	p3 = Student(name="Franco Verdi", birthdate=datetime.date(1954,1,1))
	p3.save()
	p4 = Student(name="Tommaso Bianchi", birthdate=datetime.date(1954,1,1))
	p4.save()

	# Set student insertion to their birthdate
	for h in Student.history.all():
		h.history_date = h.birthdate

	# Do some change and make story
	# In 1998 rd starts teaching os
	l1.teacher = t1
	for h in l1.history.most_recent():
		h.history_object = datetime.date(1998,1,1)

	# In 2000 j starts teaching vi
	l2.teacher = t3
	for h in l2.history.most_recent():
		h.history_object = datetime.date(2000,1,1)

	# In 2004 rd starts teaching vi
	l2.teacher = t1
	for h in l2.history.most_recent():
		h.history_object = datetime.date(2004,1,1)

	# In 1990 cb starts teaching sing
	l3.teacher = t2
	for h in l3.history.most_recent():
		h.history_object = datetime.date(1990,1,1)

	# In 1995 cb starts teaching sing
	l4.teacher = t2
	for h in l4.history.most_recent():
		h.history_object = datetime.date(1995,1,1)

	# In 2000 lf starts attending os
	p1.lecture = l1
	for h in p1.history.most_recent():
		h.history_object = datetime.date(2000,1,1)

	# In 2003 lf starts attending os
	p1.lecture = l2
	for h in p1.history.most_recent():
		h.history_object = datetime.date(2003,1,1)

	p2.lecture = l3
	p3.lecture = l1
	p4.lecture = l3

	# Change
def main():

	print("""A long time ago in a far away galaxy ... 

Someone in 1970-01-01 decides to organize the following lectures:

* Operating System (os)
* Virtual Insanity (vi)
* Singing 'Questo piccolo grande amore' (sing)
* Playing 'Questo piccolo grande amore' (play)

and to hire following teachers:

* Renzo Davoli (rd)
* Jamiroquai (j)
* Claudio Baglioni (cb)

- In 1990 cb starts teaching sing
- In 1995 cb starts teaching sing
- In 1998 rd starts teaching os
- In 2000 j starts teaching vi
- In 2004 rd starts teaching vi

Some students follow these lectures:

* Luca Ferroni (lf)
* Mario Rossi (mr)

- In 2000 lf starts attending os
- In 2003 lf starts attending os

	""")

	# Initialize some data
	teachers = Teacher.objects.all()
	students = Student.objects.all()
	lectures = Lecture.objects.all()
	if not (teachers.count() or students.count() or lectures.count()):
		init_data()

	print("The situation is...")
	for s in students:
	  print("%s" % s)

class Command(NoArgsCommand):
	help = "Initialize school demo application"
	args = ''

	option_list = BaseCommand.option_list 

	def handle(self, ws='', *args, **options):
		main()


