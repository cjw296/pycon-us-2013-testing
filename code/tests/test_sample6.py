from code.sample4 import most_owed

from testfixtures import (
    TempDirectory, LogCapture, Replacer, ShouldRaise, test_datetime
    )
from unittest import TestCase

class Tests(TestCase):

    def setUp(self):
        self.dir = TempDirectory()
        self.log = LogCapture()
        self.r = Replacer()
        self.r.replace('datetime.datetime', test_datetime())

    def tearDown(self):
        self.r.restore()
        self.log.uninstall()
        self.dir.cleanup()
        
    def test_parse(self):
        path = self.dir.write('test.csv', b'''\
Name,Money Owed
Adam Alpha,100
''')
        self.assertEqual(most_owed(path), 'Adam Alpha')
        self.log.check(('root', 'INFO', 'Processing took 0:00:10'))

    def test_max(self):
        path = self.dir.write('test.csv', b'''\
Name,Money Owed
Adam Alpha,100
Brian Beta, 300
''')
        self.assertEqual(most_owed(path), 'Brian Beta')
    
    def test_unicode(self):
        path = self.dir.write('test.csv', '''\
Name,Money Owed
C\xe9dric Cee,200
''', 'utf8')
        self.assertEqual(most_owed(path), 'C\xe9dric Cee')

    def test_whitespace(self):
        path = self.dir.write('test.csv', b'''\
Name,Money Owed
 Adam Alpha,\t100
''')
        self.assertEqual(most_owed(path), 'Adam Alpha')

    def test_invalid_numbers(self):
        path = self.dir.write('test.csv', b'''\
Name,Money Owed
Adam Alpha,X
Brian Beta, 300
''')
        self.assertEqual(most_owed(path), 'Brian Beta')
        self.log.check(
            ('root', 'WARNING', "ignoring 'X' as not valid"),
            ('root', 'INFO', 'Processing took 0:00:10')
            )

    def test_malformed(self):
        path = self.dir.write('test.csv', b'''\
Name,
Adam Alpha
''')
        with ShouldRaise(KeyError('Money Owed')):
            most_owed(path)
