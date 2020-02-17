#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# [1] 递归算法 --> 32 ms	13 MB
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.recursion(p, q)
        
    def recursion(self, p, q):
        # p和q都为None
        if not p and not q:
            return True
        # p、q只有一个是None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.recursion(p.left, q.left) and self.recursion(p.right, q.right)

# [2] 迭代算法 --> 36 ms	13.2 MB
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            # p和q都为None
            if not p and not q:
                return True
            # p、q只有一个是None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True
        # 使用队列实现迭代算法
        queue = [(p, q)]
        while(queue):
            p, q = queue.pop(0)
            if not check(p, q):
                return False
            if p:
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
        return True
            
# @lc code=end

