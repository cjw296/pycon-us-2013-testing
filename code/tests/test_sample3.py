import shutil
import tempfile
from code.sample2 import top_vol

from unittest import TestCase

class Tests(TestCase):

    def setUp(self):
        self.dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.dir)
        
    def test_parse(self):
        with tempfile.NamedTemporaryFile() as source:
            source.write(b'''\
Name,Money Owed
Adam Alpha,100
''')
            source.seek(0)
            self.assertEqual(top_vol(source.name), 'Adam Alpha')
