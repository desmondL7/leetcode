# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        stack = []
        result = []
        if root is None:
            return result
        stack.append(root)

        while len(stack) > 0:
            tmp = []
            length = len(stack)
            for i in range(length):
                r = stack.pop(0)
                tmp.append(r.val)
                if r.left: stack.append(r.left)
                if r.right: stack.append(r.right)
            result.append(tmp)

        return result