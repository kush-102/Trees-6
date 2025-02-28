# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def __init__(self):

        return

    def serialize(self, root):
        if not root:
            return ""

        sb = []
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
            if curr is not None:
                sb.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                sb.append("#")
            sb.append(",")
        return "".join(sb)
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        nodes = data.split(",")
        if not nodes or nodes[0] == "#":
            return None

        idx = 1
        q = deque()
        root = TreeNode(nodes[0])
        q.append(root)

        while q:
            curr = q.popleft()

            if idx < len(nodes) and nodes[idx] != "#":
                curr.left = TreeNode(int(nodes[idx]))
                q.append(curr.left)
            idx += 1

            if idx < len(nodes) and nodes[idx] != "#":
                curr.right = TreeNode(int(nodes[idx]))
                q.append(curr.right)
            idx += 1
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
