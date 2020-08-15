# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root):
        return self.get_depth(root,0)

    def get_depth(self,root,depth):
        if root is None:
            if depth > self.max_depth:
                self.max_depth = depth
        else:
            self.get_depth(root.left,depth+1)
            self.get_depth(root.right,depth+1)
        return self.max_depth