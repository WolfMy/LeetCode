#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归算法 --> 220 ms	86.8 MB
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:mid], postorder[:mid])
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])
        return root
''' 212 ms	51.8 MB
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return
        self.postorder = postorder
        return self.DFS(inorder)

    def DFS(self, inorder):
        root = self.postorder.pop()
        indexOfinorder = inorder.index(root)
        left_subtree = inorder[:indexOfinorder]
        right_subtree = inorder[indexOfinorder+1:]
        root = TreeNode(root)
        if right_subtree:
            root.right = self.DFS(right_subtree)
        if left_subtree:
            root.left = self.DFS(left_subtree)
        return root
'''

        
# @lc code=end

