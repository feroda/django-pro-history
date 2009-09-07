from django.core.management.base import BaseCommand, NoArgsCommand, CommandError
from optparse import make_option
import os, sys, types, re

from school.models import *
import datetime

def main():

	d = datetime.date(2010,1,1)
	print("\nToday (write 2010 if you want this) the situation is...")
	print("\n++++ Lecture snapshot at %s is ++++\n" % d )
	for l in Lecture.objects.all():
	  print("%s" % l)
	print("\n++++ Student snapshot at %s is ++++\n" % d )
	for s in Student.objects.all():
	  print("%s" % s)

	while True:

		try:
			year = int(raw_input("\nWhen are you ? (year please or EOF to exit): "))
			d = datetime.date(year,1,1)
			
			# Lecture snapshot
			print("\n++++ Lecture snapshot at %s is ++++\n" % d )
			for s in Lecture.objects.all():
				try:
					print("%s" % s.history.as_of(d))
				except Lecture.DoesNotExist, e:
					print(e)

			print("\n++++ Student snapshot at %s is ++++\n" % d )
			# Student snapshot
			for s in Student.objects.all():
				try:
					print("%s" % s.history.as_of(d))
				except Student.DoesNotExist, e:
					print(e)

		except EOFError:
			print
			break

		except Exception, e:
			print e
			
		except KeyboardInterrupt, e:
			print "\nKeyboardInterrupt ", e
			

class Command(NoArgsCommand):
	help = "Run school demo application"
	args = ''

	option_list = BaseCommand.option_list 

	def handle(self, ws='', *args, **options):
		main()


