#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# [1] 递归算法 --> 48 ms	13.3 MB
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.recursion(root.left, root.right)
    
    def recursion(self, left_subtree, right_subtree):
        if not left_subtree and not right_subtree:
            return True
        if not left_subtree or not right_subtree:
            return False
        if left_subtree.val != right_subtree.val:
            return False
        return self.recursion(left_subtree.left, right_subtree.right) and self.recursion(left_subtree.right, right_subtree.left)

# [2] 迭代算法 --> 40 ms	13.3 MB
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(left_subtree, right_subtree):
            if not left_subtree and not right_subtree:
                return True
            if not left_subtree or not right_subtree:
                return False
            if left_subtree.val != right_subtree.val:
                return False
            return True

        if not root:
            return True
        queue = [(root.left, root.right)]
        while queue:
            left_subtree, right_subtree = queue.pop(0)
            if not check(left_subtree, right_subtree):
                return False
            if left_subtree:
                queue.append((left_subtree.left, right_subtree.right))
                queue.append((left_subtree.right, right_subtree.left))
        return True

# @lc code=end

