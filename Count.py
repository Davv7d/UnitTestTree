import modules.Methods as Method
from Tree import Tree

class Count_from_tree:
    @staticmethod
    def sum_value(tree):
        if Count_from_tree.is_Tree(tree):
            return Method.total_value(tree)
        return None
    @staticmethod
    def average(tree):
        if Count_from_tree.is_Tree(tree):
            return Method.average_value(tree)
        return None

    @staticmethod
    def median(tree):
        if Count_from_tree.is_Tree(tree):
            return Method.median(tree)
        return None

    @staticmethod
    def write_results(tree):
        if Count_from_tree.is_Tree(tree):
            print("Sum: ", Count_from_tree.sum_value(tree))
            print("Average: ", Count_from_tree.average(tree))
            print("Median: ", Count_from_tree.median(tree))
        else:
            print("Object is not instance of Tree")

    @staticmethod
    def is_Tree(tree):
        if isinstance(tree, Tree):
            return True
        return False

