#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1] 迭代算法 --> 48 ms	14 MB
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [(root, root.val, [root.val])]
        while stack:
            root, current_sum, current_res = stack.pop()
            if current_sum == sum and not root.left and not root.right:
                res.append(current_res)
            if root.left:
                stack.append((root.left, current_sum+root.left.val, current_res+[root.left.val]))
            if root.right:
                stack.append((root.right, current_sum+root.right.val, current_res+[root.right.val]))
        return res
        
# @lc code=end

