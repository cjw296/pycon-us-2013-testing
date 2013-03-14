from code.sample4 import most_owed

import logging
import tempfile
from unittest import TestCase

class Tests(TestCase):

    def setUp(self):
        self.logger = logging.getLogger()
        self.original = self.logger.level
        self.logger.setLevel(1000)

    def tearDown(self):
        self.logger.setLevel(self.original)
        
    def test_parse(self):
        with tempfile.NamedTemporaryFile() as source:
            source.write(b'''\
Name,Money Owed
Adam Alpha,100
''')
            source.seek(0)
            self.assertEqual(most_owed(source.name), 'Adam Alpha')

    def test_max(self):
        with tempfile.NamedTemporaryFile() as source:
            source.write(b'''\
Name,Money Owed
Adam Alpha,100
Brian Beta, 300
''')
            source.seek(0)
            self.assertEqual(most_owed(source.name), 'Brian Beta')
    
    def test_unicode(self):
        with tempfile.NamedTemporaryFile() as source:
            source.write(bytes('''\
Name,Money Owed
C\xe9dric Cee,200
''', 'utf8'))
            source.seek(0)
            self.assertEqual(most_owed(source.name), 'C\xe9dric Cee')

    def test_whitespace(self):
        # data
        with tempfile.NamedTemporaryFile() as source:
            source.write(b'''\
Name,Money Owed
 Adam Alpha,\t100
''')
            source.seek(0)
            self.assertEqual(most_owed(source.name), 'Adam Alpha')
        # what about column headings?

    def test_invalid_numbers(self):
        with tempfile.NamedTemporaryFile() as source:
            source.write(b'''\
Name,Money Owed
Adam Alpha,X
Brian Beta, 300
''')
            source.seek(0)
            self.assertEqual(most_owed(source.name), 'Brian Beta')

    def test_malformed(self):
        # should we raise our own exception?
        with tempfile.NamedTemporaryFile() as source:
            source.write(b'''\
Name,
Adam Alpha
''')
            source.seek(0)
            try:
                most_owed(source.name)
            except Exception as e:
                self.assertTrue(isinstance(e, KeyError))
                self.assertEqual(str(e), "'Money Owed'")
            else:
                self.fail('no exception raised')
