''' python -m unittest segmenttree.tests.module_tests'''

from ..segment_tree.module import *
import unittest


class SegmentTree_Test(unittest.TestCase):
    """This is an example of a Testing class. You'll want to replace this comment with your own.
    """
    def test_size(self):
        """Test that the size attribute exists
        """
        seg = SegmentTree(10)
        self.assertEqual(hasattr(seg, "size"), True)

        segMax = SegmentTreeMax(10)
        self.assertEqual(hasattr(segMax, "size"), True)

        segSched = SegmentTreeScheduler(10)
        self.assertEqual(hasattr(segSched, "size"), True)

    # def test_single_element(self):

    # def test_odd_number_of_leaves(self):

    # def test_even_number_of_leaves(self):

    # def test_
