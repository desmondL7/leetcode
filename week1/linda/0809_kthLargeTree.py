# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode(object):
    """节点类"""
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def listcreattree(root,llist,i):###用列表递归创建二叉树，

    if i<len(llist):
        if llist[i] =='null':
            return None ###这里的return很重要
        else:
            root=TreeNode(llist[i])
            root.left=listcreattree(root.left,llist,2*i+1)
            root.right=listcreattree(root.right, llist,2*i+2)
            return root  ###这里的return很重要
    return root

llist = [1,2,3,4,5,6,7]
root=listcreattree(TreeNode(),llist,0)

class Solution:
    def __init__(self, ):
        self.curr_k = 0
        self.result = None

    def kthLargest(self, root: TreeNode, k: int) -> int:
        return self.print_tree(root, k)

    def print_tree(self, root, k):
        if root is not None:
            self.print_tree(root.right, k)
            self.curr_k = self.curr_k + 1
            if self.curr_k == k:
                self.result = root.val
            self.print_tree(root.left, k)
        return self.result
print(Solution().kthLargest(root,2))