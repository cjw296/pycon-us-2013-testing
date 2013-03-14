from code.sample1 import most_owed
from unittest import TestCase

class Tests(TestCase):

    def test_one(self):
        most_owed('foo')
