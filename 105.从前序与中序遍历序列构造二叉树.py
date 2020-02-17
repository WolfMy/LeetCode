#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归算法 --> 156 ms	51.6 MB
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        self.preorder = preorder
        return self.DFS(inorder)

    def DFS(self, inorder):
        root = self.preorder.pop(0)
        indexOfinorder = inorder.index(root)
        left_subtree = inorder[:indexOfinorder]
        right_subtree = inorder[indexOfinorder+1:]
        root = TreeNode(root)
        if left_subtree:
            root.left = self.DFS(left_subtree)
        if right_subtree:
            root.right = self.DFS(right_subtree)
        return root
''' 推荐写法
class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
'''
        
# @lc code=end

