# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# time complexity is O(n)
# space complexity is O(n)
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque()
        width_q = deque()
        hash_map = {}
        mini = 0
        maxi = 0

        q.append(root)
        width_q.append(0)

        while q:
            curr_node = q.popleft()
            curr_width = width_q.popleft()

            if curr_width not in hash_map:
                hash_map[curr_width] = []
            hash_map[curr_width].append(curr_node.val)

            if curr_node.left is not None:
                q.append(curr_node.left)
                width_q.append(curr_width - 1)
                mini = min(mini, curr_width - 1)

            if curr_node.right is not None:
                q.append(curr_node.right)
                width_q.append(curr_width + 1)
                maxi = max(maxi, curr_width + 1)

        for i in range(mini, maxi + 1):
            if i in hash_map:
                result.append(hash_map[i])
        return result
