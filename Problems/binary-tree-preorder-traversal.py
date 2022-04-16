# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root):
        numbers = []

        def get_node_item(node):
            if node is None:
                return
            else:
                numbers.append(node.val)
                get_node_item(node.left)
                get_node_item(node.right)

        get_node_item(root)
        return numbers
