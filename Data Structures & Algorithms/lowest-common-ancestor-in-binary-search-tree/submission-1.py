# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Since it's a binary tree, all values in the left subtree of a node are smaller than the nodes value
        # All values in the right subtree are greater than the node's values
        if not root or not p or not q:
            return None
        # If both values are smaller than the current node -> both must lie in the left subtree
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        # If both values are greater than the current node -> both must lie in the right subtree
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        # Where one node is on the left and one is on the right (or one is equal to current node), 
        # That split point is the Lowest Common Ancestor (LCA).
        else:
            return root

