from code.sample2 import most_owed
import tempfile
from unittest import TestCase

class Tests(TestCase):

    def test_parse(self):
        with tempfile.NamedTemporaryFile() as source:
            source.write(b'''\
Name,Money Owed
Adam Alpha,100
''')
            source.seek(0)
            self.assertEqual(most_owed(source.name), 'Adam Alpha')
