# Binary Search Tree Projesi
# [7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print("    " * level + prefix + str(node.val))
        print_tree(node.left, level + 1, prefix="L--- ")
        print_tree(node.right, level + 1, prefix="R--- ")

# Verilen dizi
arr = [7, 5, 1, 8, 3, 6, 0, 9, 4, 2]
root = None

print("BST Oluşturma Aşamaları:")
for i, value in enumerate(arr):
    root = insert(root, value)
    print(f"\nAdım {i+1}: {value} ekleniyor")
    print_tree(root)