#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1] 迭代算法 --> 40 ms	14.8 MB
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            root, current_sum = stack.pop()
            if current_sum == sum and not root.left and not root.right:
                return True
            if root.left:
                stack.append((root.left, current_sum + root.left.val))
            if root.right:
                stack.append((root.right, current_sum + root.right.val))
        return False

# [2] 递归算法 --> 44 ms	14.9 MB	
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

# @lc code=end

