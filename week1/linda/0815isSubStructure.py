# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(a,b):
            if b is None: return True
            if a is None: return False

            if a.val == b.val:
                return recur(a.left,b.left) and recur(a.right,b.right)
            return False

        return bool(A and B) and (recur(A,B) or self.isSubStructure(A.left,B) or self.isSubStructure(A.right,B))