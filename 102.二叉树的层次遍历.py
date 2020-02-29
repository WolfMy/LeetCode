#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1] 递归算法 --> 40 ms	14.1 MB
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.recursion(root, 0, res)
        return res

    def recursion(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        self.recursion(root.left, level+1, res)
        self.recursion(root.right, level+1, res)

# [2] 迭代算法 --> 52 ms	13.7 MB
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        # 队列里存储(node,level)
        queue = [(root,0)]
        while queue:
            root, level = queue.pop(0)
            if not root:
                continue
            if len(res) == level:
                res.append([])
            res[level].append(root.val)
            queue.append((root.left, level+1))
            queue.append((root.right, level+1))
        return res

# @lc code=end

