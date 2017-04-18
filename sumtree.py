#!/usr/bin/env python3

class BinaryTree(object):
    def __init__(self, center, left=None, right=None):
        self.center = center
        self.left = left
        self.right = right

    def __str__(self):
        s = str(self.center) + "\n"
        if self.left is not None:

            s += str(self.left)
        if self.right is not None:
            s += str(self.right)

        return s

    def to_sum_tree(self):
        if self.left is None and self.right is None:
            return BinaryTree(0)

        center = 0
        left = None
        if self.left is not None:
            left = self.left.to_sum_tree()
            center += left.center + self.left.center

        right = None
        if self.right is not None:
            right = self.right.to_sum_tree()
            center += right.center + self.right.center

        return BinaryTree(center, left, right)

    def sum(self):
        s = 0
        if self.left is not None:
            s += self.left.sum() + self.left.center
        if self.right is not None:
            s += self.right.sum() + self.right.center

        return s

    def is_sum_tree(self):
        if self.left is None and self.right is None:
            return True

        if self.sum() != self.center:
            return False

        if self.left is not None and not self.left.is_sum_tree():
            return False

        if self.right is not None and not self.right.is_sum_tree():
            return False

        return True

tree = BinaryTree(10,
            BinaryTree(-2, BinaryTree(8), BinaryTree(-4)),
            BinaryTree(6, BinaryTree(7), BinaryTree(5)))

# print(tree.to_sum_tree())

sum_tree = BinaryTree(26,
                      BinaryTree(10, BinaryTree(4), BinaryTree(6)),
                      BinaryTree(3, None, BinaryTree(3)))

print(tree.is_sum_tree(), "should be False")
print(sum_tree.is_sum_tree(), "should be True")
