#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1] 递归算法 --> 80 ms	14.9 MB
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.DFS(root)

    def DFS(self, root):
        if not root.left and not root.right:
            return 1
        left_height = self.DFS(root.left) + 1 if root.left else float('inf')
        right_height = self.DFS(root.right) + 1 if root.right else float('inf')
        return min(left_height, right_height)

# [2] 迭代算法 --> 44 ms	14.1 MB
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0 
        queue = [(root, 1)]
        min_depth = float('inf')
        while queue:
            root, depth = queue.pop(0)
            if not root.left and not root.right:
                min_depth = min(min_depth, depth)
                continue
            if root.left:
                queue.append((root.left, depth+1))
            if root.right:
                queue.append((root.right, depth+1))
        return min_depth
        
# @lc code=end

