import unittest

from Tree import Tree
from Count import Count_from_tree as Count

class Test_Tree(unittest.TestCase):
    tree_example_table = []
    def fill_tree_table(self):
        '''file tree table with examples'''
        self.tree_example_table.append(Tree(8, [Tree(7, [Tree(6), Tree(5), Tree(4)]), Tree(3, [Tree(2, [Tree(1)])])]))
        self.tree_example_table.append(Tree(8, [Tree(7), Tree(3, [Tree(2, [Tree(1, [Tree(6), Tree(5, [Tree(4)])])])])]))
        self.tree_example_table.append(Tree(83, [Tree(-41, [Tree(-15), Tree(26), Tree(-74), Tree(-77), Tree(-85), Tree(-11), Tree(-51), Tree(-99), Tree(-95), Tree(-42), Tree(-100), Tree(-87), Tree(-98), Tree(-30), Tree(4), Tree(-93, [Tree(17, [Tree(74, [Tree(78), Tree(27), Tree(68)])])])]), Tree(85, [Tree(-76), Tree(-17), Tree(-12), Tree(-59)]), Tree(60, [Tree(-52, [Tree(22), Tree(93)])])]))
        self.tree_example_table.append(Tree(-18, [Tree(12, [Tree(0, [Tree(6, [Tree(-2, [Tree(12, [Tree(-4, [Tree(8)])])])])])])]))
        self.tree_example_table.append(Tree(-65, [Tree(-47, [Tree(52), Tree(-76)]),Tree(-82, [Tree(-46, [Tree(-10, [Tree(44)])])]), Tree(-53, [Tree(-88), Tree(-39)])]))
        self.tree_example_table.append(Tree(13, [Tree(46), Tree(81), Tree(-13), Tree(72, [Tree(-45)]), Tree(10),Tree(24, [Tree(-47), Tree(86), Tree(83)]), Tree(21), Tree(75, [Tree(-35), Tree(-6)]), Tree(94)]))
        self.tree_example_table.append(Tree(-20, [Tree(-7, [Tree(31), Tree(-19, [Tree(77)])]), Tree(40, [Tree(27, [Tree(58), Tree(88, [Tree(35)])])])]))

    def test_correct_value(self):
        """test checking if correct data is returned by methods:
                sum value
                average
                median
            """
        self.fill_tree_table()
        self.assertEqual(
            (Count.sum_value(self.tree_example_table[0]), Count.average(self.tree_example_table[0]), Count.median(self.tree_example_table[0])),
            (36, 4.5, 4.5))
        self.assertEqual(
            (Count.sum_value(self.tree_example_table[1]), Count.average(self.tree_example_table[1]),
             Count.median(self.tree_example_table[1])),
            (36, 4.5, 4.5))
        self.assertEqual(
            (Count.sum_value(self.tree_example_table[2]), Count.average(self.tree_example_table[2]),
             Count.median(self.tree_example_table[2])),
            (-577, -18.03125, -23.5))
        self.assertEqual(
            (Count.sum_value(self.tree_example_table[3]), Count.average(self.tree_example_table[3]),
             Count.median(self.tree_example_table[3])),
            (14, 1.75, 3))
        self.assertEqual(
            (Count.sum_value(self.tree_example_table[4]), Count.average(self.tree_example_table[4]),
             Count.median(self.tree_example_table[4])),
            (-410, -37.27272727272727, -47))
        self.assertEqual(
            (Count.sum_value(self.tree_example_table[5]), Count.average(self.tree_example_table[5]),
             Count.median(self.tree_example_table[5])),
            (459, 28.6875, 22.5))
        self.assertEqual(
            (Count.sum_value(self.tree_example_table[6]), Count.average(self.tree_example_table[6]),
             Count.median(self.tree_example_table[6])),
            (310, 31, 33))

    def test_incorrect_value_None(self):
        """test checking if None data is returned by methods on None:
                sum value
                average
                median
            """
        self.assertEqual(Count.median(None), None)
        self.assertEqual(Count.sum_value(None), None)
        self.assertEqual(Count.average(None), None)

    def test_incorrect_value_String(self):
        """test checking if None data is returned by methods on String:
                sum value
                average
                median
            """
        self.assertEqual(Count.median("adsd"), None)
        self.assertEqual(Count.sum_value("123"), None)
        self.assertEqual(Count.average("dasd"), None)

    def test_incorrect_value_int(self):
        """test checking if None data is returned by methods on  int:
                sum value
                average
                median
            """
        self.assertEqual(Count.median(312), None)
        self.assertEqual(Count.sum_value(11), None)
        self.assertEqual(Count.average(222), None)

    def test_tree_setBranch_correct(self):
        """test setBranch correct date"""
        tree1 = self.tree_example_table[0]
        self.assertTrue(tree1.setBranch(Tree(23)))

    def test_tree_setBranch_incorrect_branches(self):
        """test setBranch incorrect with tree with multiple branches """
        tree1 = self.tree_example_table[0]
        self.assertFalse(tree1.setBranch(self.tree_example_table[2]))

    def test_tree_setBranch_incorrect_value(self):
        """test setBranch incorrect int, string, none, boolen """
        tree1 = self.tree_example_table[0]
        self.assertFalse(tree1.setBranch(1))
        self.assertFalse(tree1.setBranch("asd"))
        self.assertFalse(tree1.setBranch(None))
        self.assertFalse(tree1.setBranch(True))

    def test_tree_deleteBranch_correct(self):
        """test deleteBranch correct date"""
        tree1 = self.tree_example_table[0]
        self.assertTrue(tree1.deleteBranch(1))

    def test_tree_deleteBranch_incorrect_value(self):
        """test deleteBranch incorrect string, none, boolen, tree  """
        tree1 = self.tree_example_table[0]
        self.assertFalse(tree1.deleteBranch("asd"))
        self.assertFalse(tree1.deleteBranch(None))
        self.assertFalse(tree1.deleteBranch(True))
        self.assertFalse(tree1.deleteBranch(self.tree_example_table[2]))

    def test_tree_getBranchcorrect(self):
        """test getBranch correct date"""
        tree1 = self.tree_example_table[0]
        self.assertTrue(isinstance(tree1.getBranch(0), Tree))

    def test_tree_getBranch_incorrect_value(self):
        """test getBranch incorrect string, none, boolen, tree  """
        tree1 = self.tree_example_table[0]
        self.assertFalse(tree1.getBranch("asd"))
        self.assertFalse(tree1.getBranch(None))
        self.assertFalse(tree1.getBranch(True))
        self.assertFalse(tree1.getBranch(self.tree_example_table[2]))

if __name__ == "__main__":
    unittest.main()
