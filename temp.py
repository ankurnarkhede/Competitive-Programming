import sys


def read_single_integer():
    return int (sys.stdin.readline ().strip ())


def read_array_of_integers():
    return list (map (int, sys.stdin.readline ().strip ().split ()))


def read_single_string():
    return sys.stdin.readline ().strip ()


class Node:
    def _init_(self, value):
        self.val = value
        self.left = None
        self.right = None

    def get(self):
        return self.val

    def set(self, val):
        self.val = val

    def get_children(self):
        children = []
        if self.left is not None:
            children.append (self.left)
        if self.right is not None:
            children.append (self.right)
        return children


class BST:
    def _init_(self):
        self.root = None

    def set_root(self, val):
        self.root = Node (val)

    def insert(self, val):
        if self.root is None:
            self.set_root (val)
        else:
            self.insert_node (self.root, val)

    def insert_node(self, curret_node, val):
        if val <= curret_node.val:
            if curret_node.left:
                self.insert_node (curret_node.left, val)
            else:
                curret_node.left = Node (val)
        elif val > curret_node.val:
            if curret_node.right:
                self.insert_node (curret_node.right, val)
            else:
                curret_node.right = Node (val)

    def lca(self, x, y):
        p = self.root
        while (p.val > x and p.val > y) or (p.val < x and p.val < y):
            if x < p.val and y < p.val:
                p = p.left
            elif x > p.val and y > p.val:
                p = p.right
        return p

    def max_on_path(self, start_node, x):
        maxi = 0
        while start_node.val != x:
            if start_node.val > x:
                maxi = max (maxi, start_node.val)
                start_node = start_node.left
            elif start_node.val < x:
                maxi = max (maxi, start_node.val)
                start_node = start_node.right
        return max (maxi, x)

    def inorder_traverse(self, node):
        if node:
            self.inorder_traverse (node.left)
            print (node.val)
            self.inorder_traverse (node.right)

    def traverse(self):
        if self.root:
            self.inorder_traverse (self.root)

    def depth_util(self, node):
        if node is None:
            return 0
        left_subtree_depth = self.depth_util (node.left) + 1
        right_subtree_depth = self.depth_util (node.right) + 1
        return max (left_subtree_depth, right_subtree_depth)

    def depth(self):
        if self.root:
            return self.depth_util (self.root)
        return 0

    def get_node_util(self, node, value):
        if node is None:
            return None
        elif node.val == value:
            return node
        elif node.left.val >= value:
            return self.get_node_util (node.left, value)
        elif node.left.val < value:
            return self.get_node_util (node.right, value)

    def get_node(self, value):
        if self.root:
            return self.get_node_util (self.root, value)
        return None

    def pre_order_traverse(self, node):
        if node:
            print (node.val)
            self.pre_order_traverse (node.left)
            self.pre_order_traverse (node.right)


sys.setrecursionlimit (1500)

n = read_single_integer ()
array = read_array_of_integers ()
bst = BST ()
for ele in array:
    bst.insert (ele)
x, y = read_array_of_integers ()
lca = bst.lca (x, y)
# bst.traverse()
# print(lca.val)
print (max (bst.max_on_path (lca, x), bst.max_on_path (lca, y)))
