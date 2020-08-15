# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self, ):
        self.curr_k = 0

    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.print_tree(root, k)

    def print_tree(self, root, k):
        if root is None:
            return root
        self.print_tree(root.right, k)
        self.curr_k = self.curr_k + 1
        if self.curr_k == k:
            return root.val
        self.print_tree(root.left, k)
