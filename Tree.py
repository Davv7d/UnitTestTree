class Tree:

    def __init__(self, data, branches=[]):
        if not isinstance(data, int):
            raise ValueError("invalid data")
        for branch in branches:
            if not isinstance(branch, Tree):
                raise ValueError("invalid branch")

        self.data = data
        self.branches = branches

    def __str__(self):
        return str(self.data)

    def setBranch(self, tree):
        """ set new branch to tree """

        if tree == None:
            return False
        if isinstance(tree, Tree):
            if len(tree.branches) > 0:
                return False
            if len(self.branches) > 0:
                self.branches.append(tree)
            else:
                self.branches = [tree]
            return True
        return False

    def getBranch(self, id):
        """ get branch by id """

        if isinstance(id, int):
            if id >= 0:
                if len(self.branches) > id:
                    return self.branches[id]
        return None

    def deleteBranch(self, id):
        """ delete branch from tree """

        if isinstance(id, int):
            if id >= 0:
                if len(self.branches) > id:
                    del self.branches[id]
                    return True
        return False
