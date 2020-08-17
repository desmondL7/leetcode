from  create_tree_from_list import *
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res.append(None)
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1].split(',')
        print(data)
        root = TreeNode(data[0])
        q = [root]
        index = 1
        while q:
            node = q.pop(0)
            if index < len(data):
                node.left = TreeNode(data[index])
                q.append(node.left)
            if index + 1 < len(data):
                node.right = TreeNode(data[index + 1])
                q.append(node.right)
            index += 2
        return root

[1,2,3,null,null,4,5]