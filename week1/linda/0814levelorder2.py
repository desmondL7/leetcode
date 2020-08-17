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
        row = 0
        while len(level) > 0:
            tmp = []
            tmp1 = []
            while len(level) > 0:
                i = level.pop(0)
                tmp1.append(i.val)
                if i.left:
                    tmp.append(i.left)
                if i.right:
                    tmp.append(i.right)
            if row%2==0:
                res.append(tmp1)
            else:
                tmp1.reverse()
                res.append(tmp1)
            level = tmp
            row += 1
        return res


