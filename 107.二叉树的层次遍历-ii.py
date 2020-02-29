#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1] 递归算法 --> 64 ms	14.1 MB
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        self.BFS(root, 0, res)
        res.reverse()
        return res

    def BFS(self, root, level, res):        
        if len(res) == level:
            res.append([])
        
        res[level].append(root.val)
        if root.left:
            self.BFS(root.left, level+1, res)
        if root.right:
            self.BFS(root.right, level+1, res)

# [2] 迭代算法 --> 32 ms	13.7 MB
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = [(root, 0)]
        while queue:
            root, level = queue.pop(0)
            if len(res) == level:
                res.append([])
            
            res[level].append(root.val)
            if root.left:
                queue.append((root.left, level+1))
            if root.right:
                queue.append((root.right, level+1))
        res.reverse()
        return res

# @lc code=end

