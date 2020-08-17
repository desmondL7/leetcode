# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.dict, self.preorder = {}, preorder
        for i, val in enumerate(inorder):
            self.dict[val] = i
        return self.rec(0, 0, len(inorder) - 1)

    def rec(self, pre_root, in_left, in_right):
        if in_left > in_right:
            return None
        root = TreeNode()
        root.val = self.preorder[pre_root]
        in_root_index = self.dict[root.val]
        root.left = self.rec(pre_root + 1, in_left, in_root_index - 1)
        root.right = self.rec(pre_root + in_root_index - in_left + 1, in_root_index + 1, in_right)
        return root