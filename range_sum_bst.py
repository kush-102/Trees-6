# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.helper(root, low, high)
        return self.result

    def helper(self, root: TreeNode, low: int, high: int) -> None:
        if root is None:
            return

        if root.val < low:
            self.helper(root.right, low, high)
            return

        if root.val > high:
            self.helper(root.left, low, high)
            return

        self.result += root.val

        self.helper(root.left, low, high)
        self.helper(root.right, low, high)


# Time Complexity: O(h + k)
# h is the height of the tree
# k is the number of nodes within the range [low, high]
# space complexity is O(h)


# int based recursion
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        current_sum = root.val
        left_sum = self.rangeSumBST(root.left, low, high)
        right_sum = self.rangeSumBST(root.right, low, high)

        return current_sum + left_sum + right_sum
