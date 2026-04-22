# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        array = [root]
        ans = []
        while array:
            arr = []
            for _ in range(len(array)):
                i = array.pop(0)
                arr.append(i.val)
                if i.left: array.append(i.left)
                if i.right: array.append(i.right)
            ans.append(arr)
        return ans