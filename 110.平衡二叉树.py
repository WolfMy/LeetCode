#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1] 递归算法（自顶向下） --> 68 ms	16.7 MB
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 从根结点开始判断是否是平衡二叉树
        if not root:
            return True
        if abs(self.getDepth(root.left) - self.getDepth(root.right)) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def getDepth(self, root):
        # 递归获取当前结点的最大深度
        if not root:
            return 0
        left_height = self.getDepth(root.left) + 1
        right_height = self.getDepth(root.right) + 1
        return max(left_height, right_height)

# [2] 递归算法（自底向上） --> 48 ms	17 MB
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isSubtreeBalanced(root)[1]
        
    def isSubtreeBalanced(self, root):
        # 从叶子结点开始判断是否是平衡二叉树
        if not root:
            return 0, True
        left_height, left_isBalanced = self.isSubtreeBalanced(root.left)
        if not left_isBalanced:
            return 0, False
        right_height, right_isBalanced = self.isSubtreeBalanced(root.right)
        if not right_isBalanced:
            return 0, False
        return max(left_height, right_height) + 1, abs(left_height - right_height) <= 1
        


        
# @lc code=end

