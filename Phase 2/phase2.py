"""
@author: EDA Team
"""

# Classes provided by EDA Team
from bintree import BinaryNode
from bst import BinarySearchTree


# Exercise #1
class BST2(BinarySearchTree):
    def find_dist_k(self, n: int, k: int) -> list:
        # First find the node with element "n"
        node = self.search(n)
        # Create the python list you will return
        klist = []

        if node is not None:
            klist = self._find_dist_k(node, k, klist)

        return klist

    def _find_dist_k(self, node, k, klist):
        # If "k" is zero that means that the node we found before
        # is at the distance we want so append to the list the element
        if node is not None:
            if k == 0:
                klist.append(node.elem)
            else:
                klist_left = self._find_dist_k(node.left, k - 1, klist)
                klist_right = self._find_dist_k(node.right, k - 1, klist)
                klist = list(set(klist_left) | set(klist) | set(klist_right))

        return klist


# Exercise #2
    def create_tree(self, input_tree1: BinarySearchTree, input_tree2: BinarySearchTree, opc: str) -> BinarySearchTree:
        # generate an empty tree
        new_tree = BinarySearchTree()
        if opc == 'merge':
            new_tree = input_tree1
            self.difference(input_tree1, new_tree, input_tree2.root)
        elif opc == 'intersection':
            return self.intersection(input_tree2, new_tree, input_tree1.root)
        elif opc == 'difference':
            return self.difference(input_tree2, new_tree, input_tree1.root)
        else:
            raise ValueError('Invalid opc parameter')

    def difference(self, new_tree: BinarySearchTree, tree: BinarySearchTree, node: BinaryNode):
        if not node:
            return

        if not tree.search(node.elem):
            new_tree.insert(node.elem)

        self.difference(tree, new_tree, node.left)
        self.difference(tree, new_tree, node.right)

    def intersection(self, tree: BinarySearchTree, new_tree: BinarySearchTree, node: BinaryNode):
        if not node:
            return

        if tree.search(node.elem):
            new_tree.insert(node.elem)

        self.intersection(tree, new_tree, node.left)
        self.intersection(tree, new_tree, node.right)


# Some usage examples
if __name__ == '__main__':
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]
    input_list_01 = [5, 12, 2, 1, 3, 9]
    input_list_02 = [9, 3, 21]

    # Build and draw first tree
    tree1 = BinarySearchTree()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()

    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    tree2.draw()

    function_names = ["merge", "intersection", "difference"]

    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- Result for {op_name} method. #{res.size()} nodes")
        res.draw()
