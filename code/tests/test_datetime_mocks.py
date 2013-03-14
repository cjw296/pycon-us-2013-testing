from testfixtures import OutputCapture
from unittest import TestCase

from testfixtures import test_datetime

class TestDateTime(TestCase):

    def test_simple(self):
        with OutputCapture() as output:

            datetime = test_datetime()
            print(datetime.now())
            print(datetime.now())
            print(datetime.now())

        output.compare('''
2001-01-01 00:00:00
2001-01-01 00:00:10
2001-01-01 00:00:30
''')
        
    def test_specific(self):
        with OutputCapture() as output:

            datetime = test_datetime(None)
            datetime.add(1978, 6, 13, 16, 0, 1)
            datetime.add(2013, 3, 23, 14, 30)
            print(datetime.now())
            print(datetime.now())

        output.compare('''
1978-06-13 16:00:01
2013-03-23 14:30:00
''')
        
            
    def test_delta(self):
        with OutputCapture() as output:

            datetime = test_datetime(delta=2, delta_type='hours')
            print(datetime.now())
            print(datetime.now())

        output.compare('''
2001-01-01 00:00:00
2001-01-01 02:00:00
''')
        
from testfixtures import test_date

class TestDate(TestCase):

    def test_simple(self):
        with OutputCapture() as output:

            date = test_date(2013, 3, 23)
            print(date.today())
            print(date.today())
            print(date.today())

        output.compare('''
2013-03-23
2013-03-24
2013-03-26
''')
        
    def test_specific(self):
        with OutputCapture() as output:

            date = test_date(None)
            date.add(1978, 6, 13)
            date.add(2013, 3, 23)
            print(date.today())
            print(date.today())

        output.compare('''
1978-06-13
2013-03-23
''')
        
            
    def test_delta(self):
        with OutputCapture() as output:

            date = test_date(delta=2, delta_type='days')
            print(date.today())
            print(date.today())

        output.compare('''
2001-01-01
2001-01-03
''')
        
from testfixtures import test_time

class TestTime(TestCase):

    def test_simple(self):
        with OutputCapture() as output:

            time = test_time()
            print(time())
            print(time())
            print(time())

        output.compare('''
978307200.0
978307201.0
978307203.0
''')
        
    def test_specific(self):
        with OutputCapture() as output:

            time = test_time(None)
            time.add(1978, 6, 13, 16, 1)
            time.add(2013, 3, 23, 14, 30)
            print(time())
            print(time())

        output.compare('''
266601660.0
1364049000.0
''')
        
            
    def test_delta(self):
        with OutputCapture() as output:

            time = test_time(delta=0.5, delta_type='seconds')
            print(time())
            print(time())

        output.compare('''
978307200.0
978307200.5
''')
        
