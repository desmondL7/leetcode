# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root :
            stack = [root.left,root.right]
            while len(stack)>0:
                a = stack.pop(0)
                b = stack.pop(0)
                if a == None and b == None:
                    continue
                if a == None or b == None:
                    return False
                if a.val != b.val:
                    return False
                stack.append(a.left)
                stack.append(b.right)
                stack.append(a.right)
                stack.append(b.left)
        return True