import tempfile
from code.sample2 import top_vol

from unittest import TestCase

class Tests(TestCase):

    def test_parse(self):
        with tempfile.NamedTemporaryFile() as source:
            source.write(b'''\
Name,Money Owed
Adam Alpha,100
''')
            source.seek(0)
            self.assertEqual(top_vol(source.name), 'Adam Alpha')

    def test_max(self):
        with tempfile.NamedTemporaryFile() as source:
            source.write(b'''\
Name,Money Owed
Adam Alpha,100
Brian Beta, 300
''')
            source.seek(0)
            self.assertEqual(top_vol(source.name), 'Adam Alpha')
    
    def test_unicode(self):
        pass

    def test_invalid_numbers(self):
        pass

    def test_negative_numbers(self):
        pass

    def test_whitespace(self):
        # column headings
        # data
        pass

    def test_malformed(self):
        # should we have our own exception?
        pass
