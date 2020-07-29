#  I

def total_value(tree):
    '''sum of values in a given subtree/tree'''

    if tree == None:
        return 0
    result = tree.data
    for branch in tree.branches:
        result += total_value(branch)
    return result


#  II

def total_branches_number(tree):
    '''sum of branches in given subtree/tree'''

    if tree == None:
        return 0
    result = 1
    for branch in tree.branches:
        result += total_branches_number(branch)
    return result

def average_value(tree):
    '''average value in given subtree/tree'''

    if tree == None:
        return 'Error'
    sum_value = total_value(tree)
    sum_branches = total_branches_number(tree)
    return sum_value / sum_branches


#  III

def tree_to_list(tree,list = []):
    '''parsing tree to list '''

    if tree == None:
        return []
    list.append(tree.data)
    for branch in tree.branches:
        tree_to_list(branch, list)
    return list


def median(tree):
    '''counting median'''
    tree_list = tree_to_list(tree, [])
    tree_list.sort()
    length = len(tree_list)
    # print(tree_list)
    if (length%2 == 1):
        return tree_list[int(length/2)]
    else:
        value = (tree_list[int( length/2) - 1] + tree_list[int( length/2)]) /2
        return value
