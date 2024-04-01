"""
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst
"""
from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(min(height, k))
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def _kthSmallest(node, depth=1):
            nonlocal k
            if node.left:
                result = _kthSmallest(node.left, depth)
                if result is not None:
                    return result
            k -= 1
            if k == 0:
                return node.val
            if node.right:
                result = _kthSmallest(node.right, depth)
                if result is not None:
                    return result

        return _kthSmallest(root)


# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(6)
# root.left.left = TreeNode(2)
# root.left.right = TreeNode(4)
# root.left.left.left = TreeNode(1)

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)
print(Solution().kthSmallest(root, 7))
