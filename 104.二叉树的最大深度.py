#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1] 递归算法 --> 32 ms	14.5 MB
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.DFS(root)

    def DFS(self, root):
        if not root:
            return 0
        
        left_depth = self.DFS(root.left) + 1
        right_depth = self.DFS(root.right) + 1
        return max(left_depth, right_depth)

# [2] 迭代算法 --> 48 ms	14.2 MB
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        # 栈存储当前深度和结点
        stack = [(1, root)]
        max_depth = 1
        while stack:
            depth, root = stack.pop()
            if root:
                max_depth = max(max_depth, depth)
                stack.append((depth+1, root.left))
                stack.append((depth+1, root.right))
        return max_depth

# @lc code=end

