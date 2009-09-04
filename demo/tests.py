"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

__test__ = {"doctest": """
Another way to test that 1 + 1 is equal to 2.

>>> from demo.models import *
>>> import datetime
>>> d = datetime.date(2007,1,1)
>>> p = Person.objects.all()[0]
>>> p2007 = p.history.as_of(d)
>>> p2007.roles.all()[0]
<OrgRole: Luca Ferroni `fero` (1) in LABS (30) (leader)>

"""}

"""
In [6]: p = Person(name='Luca Ferroni', nick='bobo', nsons=0)

In [7]: import datetime

In [8]: p.birthdate = datetime.date(1980,2,17)

In [9]: p.save()

In [10]: p.nick="fero"

In [11]: p.save()

In [12]: w = Person(name='Eleonora Latini', nsons=0)

In [13]: w.birthdate = datetime.date(1982,6,20)

In [14]: w.save()

In [15]: w.nick = "winny"

In [16]: w.save()

In [17]: p.wife = w 

In [18]: p.nsons = 1

In [19]: p.save()

In [20]: w.nsons = 1

In [21]: w.save()

In [12]: ph = p.history.all()[2]

In [13]: ph.hi
ph.history_date     ph.history_object   ph.history_user     
ph.history_id       ph.history_type     ph.history_user_id  

In [13]: ph.history_date
Out[13]: datetime.datetime(2009, 8, 28, 17, 22, 51, 327028)

In [14]: import datetime

In [15]: ph.hi
ph.history_date     ph.history_object   ph.history_user     
ph.history_id       ph.history_type     ph.history_user_id  

In [15]: ph.history_date = datetime.datetime(1999, 1, 1, 17, 22, 51)

In [16]: ph.save()

In [34]: ph = p.history.all()[1]

In [35]: ph.nick
Out[35]: u'fero'

In [36]: ph.wife

In [37]: ph.history_date = datetime.datetime(2003, 1, 1, 17, 22, 51)

In [38]: ph.save()

In [40]: ph = p.history.all()[0]

In [41]: ph.history_date = datetime.datetime(2009, 5, 26, 17, 51, 51)

In [42]: ph.save()

In [49]: ph = w.history.all()[2]

In [50]: ph.history_date = datetime.datetime(1982, 6, 20, 17, 22, 51)

In [51]: ph.save()

In [52]: ph = w.history.all()[1]

In [53]: ph.history_date = datetime.datetime(1996, 12, 28, 17, 22, 51)

In [54]: ph.save()

In [55]: ph = w.history.all()[0]

In [56]: ph.history_date = datetime.datetime(2009, 5, 26, 17, 51, 51)

In [57]: ph.save()

In [134]: orgr = OrgRole(person=p, org=o, role="developer")

In [135]: orgr.save()

In [136]: orgr.role='leader'

In [137]: orgr.save()

In [138]: orgrh = orgr.history.all()[1]

In [139]: orgrh.history_date = datetime.datetime(2004, 10, 20, 17, 51, 51)

In [140]: orgrh.save()

In [141]: orgrh = orgr.history.all()[0]

In [142]: orgrh.history_date = datetime.datetime(2009, 06, 12, 17, 51, 51)

In [143]: orgrh.save()

In [144]: orgr.delete()

In [145]: oh = o.history.all()[1]

In [146]: oh.history_date = datetime.datetime(2004, 01, 01, 17, 51, 51)

In [147]: oh.save()

195: d = datetime.date(2001,1,1)
196: p2001 = p.history.as_of(d)
197: p2001.orgrole_set.all()[0].role
198: orgrole.history.as_of(d)
199: orgr.history.as_of(d)
200: d = datetime.date(2008,1,1)
201: orgr.history.as_of(d)
202: orgr.history.as_of(d).role
203: p2008 = p.history.as_of(d)
204: p2008.orgrole_set.all()[0].role
205: p2008.wife
206: orgr.history.as_of(d).role
207: orgr.history.as_of(d).person
208: orgr.history.as_of(d).person.name
209: orgr.history.as_of(d).wife
210: orgr.history.as_of(d).person.wife
211: d
212: orgr.history.as_of(d).org.nemployers

d e' il 2008 !
AAAA QUESTO NON FUNZIONA ! 
230: d 
231: p2008 = p.history.as_of(d)
232: p2008
233: p2008.wife
'non ho moglie'
235: p2008.orgrole_set.all()[0].role
'leader'
236: orgr.history.as_of(d)
237: orgr.history.as_of(d).role
'developer'

"""
