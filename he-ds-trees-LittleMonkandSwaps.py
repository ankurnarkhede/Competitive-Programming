
import sys

binary_inorder=[]

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root


    def add_linearly(self, arr, node, index, size):

        if (index < size):
            node = Node (arr[index])

            # insert left child
            node.left =  tree.add_linearly(arr, node.left, 2 * index + 1, size )

            # insert right child
            node.right = tree.add_linearly(arr, node.right, 2 * index + 2, size )

        return node


    def get_in_order(self, node):
        # getting inorder array in var
        if (node != None):
            self.get_in_order (node.left)
            binary_inorder.append (node.data)
            self.get_in_order (node.right)
        return binary_inorder


# main

if __name__=='__main__':
    try:
        n = int (input().strip())

    except(Exception):
        n = int (sys.stdin.readline ().strip ())

    a = (list (map (int, sys.stdin.readline ().strip ().split (' '))))


    tree = Tree ()

    tree.root=tree.add_linearly(a,tree.getRoot(),0,len(a))

    binary_inorder =  tree.get_in_order(tree.getRoot())
    A=list(binary_inorder)
    A.sort ()

    M = {}
    for i in range (len (A)):
        M[A[i]] = i
    check = {}


    def cycleSize(index):
        size = 1
        i = M[binary_inorder[index]]
        check[i] = 1
        while i != index:
            i = M[binary_inorder[i]]
            check[i] = 1
            size += 1
        return size


    total = 0
    for i in range (len (binary_inorder)):
        if i not in check:
            total += cycleSize (i) - 1
    print (total)

