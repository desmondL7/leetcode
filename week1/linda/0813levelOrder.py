# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        level = [root]
        while len(level) > 0:
            tmp = []
            while len(level) > 0:
                i = level.pop(0)
                res.append(i.val)
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            level = tmp
        return res


