from collections import namedtuple
from unittest import TestCase

DataRow = namedtuple('DataRow', ('x', 'y', 'z'))

class TestDataRow(TestCase):

    def test_different(self):
        self.addTypeEqualityFunc(DataRow, self.assertSequenceEqual)
        self.assertEqual(DataRow(1, 2, 3), DataRow(1, 2, 4))
