"""
297. Serialize and Deserialize Binary Tree
https://leetcode.com/problems/serialize-and-deserialize-binary-tree
"""
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        remaining = deque([root])
        data = []
        while remaining:
            curr = remaining.popleft()
            if curr is None:
                data.append("null")
                continue
            data.append(str(curr.val))
            remaining.append(curr.left)
            remaining.append(curr.right)
        return f"[{','.join(data)}]"

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1].split(',')
        if data[0] == "null":
            return None
        root = TreeNode(data[0])
        remaining = deque([root])
        index = 1

        while remaining:
            curr = remaining.popleft()
            if index < len(data) and data[index] != "null":
                curr.left = TreeNode(data[index])
                remaining.append(curr.left)
            index += 1
            if index < len(data) and data[index] != "null":
                curr.right = TreeNode(data[index])
                remaining.append(curr.right)
            index += 1

        return root


ser = Codec()
deser = Codec()
ans = ser.deserialize("[1,2,3,null,null,4,5]")
print(ser.serialize_recursive(ans))
