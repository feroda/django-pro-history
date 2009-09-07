from django.core.management.base import BaseCommand, NoArgsCommand, CommandError
from optparse import make_option
import os, sys, types, re

from school.models import *
import datetime

def main():

	while True:

		try:
			year = int(raw_input("When are you ? (only year please): "))
			d = datetime.date(year,1,1)
			
			print("At %s the situation is..." % d)
			for s in Student.objects.all():
				try:
					print("%s" % s.history.as_of(d))
				except Student.DoesNotExist, e:
					print(e)
		except EOFError:
			print
			break

class Command(NoArgsCommand):
	help = "Run school demo application"
	args = ''

	option_list = BaseCommand.option_list 

	def handle(self, ws='', *args, **options):
		main()


