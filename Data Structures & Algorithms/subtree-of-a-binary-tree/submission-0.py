# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def issubTree(t1, t2):
            if not t2 and not t1: return True
            if not t1 and t2: return False
            if t1 and t2 and t1.val == t2.val:
                return issubTree(t1.left, t2.left) and issubTree(t1.right, t2.right)
            return False

        def dfs(root1, root2):
            if not root2: return True
            if not root1: return False
            print(root1.val, root2.val)
            if issubTree(root1, root2): return True
            return dfs(root1.left, root2) or dfs(root1.right, root2)
        return dfs(root, subRoot)
