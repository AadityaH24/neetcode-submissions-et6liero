# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = [root]
        res = []
        
        while q:
            row_len = len(q)
            for i in range(row_len):
                
                node = q.pop(0)
                if i == row_len - 1:
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res


    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        res = self.helper(root)

        return res