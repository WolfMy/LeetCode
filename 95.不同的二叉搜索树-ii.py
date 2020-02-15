#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# [1] 递归算法 --> 52 ms	14.3 MB
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0:
            return []
        all_trees = self.recursion(1, n)
        return all_trees

    def recursion(self, start, end):
        if start > end:
            return [None]
        trees = []
        for i in range(start, end+1):
            left = self.recursion(start, i-1)
            right = self.recursion(i+1,end)
            for l in left:
                for r in right:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    trees.append(root)
        return trees

        
# @lc code=end

