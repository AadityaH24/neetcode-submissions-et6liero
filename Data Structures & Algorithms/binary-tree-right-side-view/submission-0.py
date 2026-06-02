# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(lvl, node, depth):
            if not node:
                return

            if depth not in lvl:
                lvl[depth] = []
            lvl[depth].append(node.val)
            # print(depth, node.val, lvl)
            preorder(lvl, node.left, depth + 1)
            preorder(lvl, node.right, depth + 1)
            
        res = {}
        preorder(res, root, 0)
        # print(res)
        return res
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        lvlOrder = self.helper(root)
        out = []
        for k,v in lvlOrder.items():
            # print(k,v)
            out.append(v[-1])
        return out
