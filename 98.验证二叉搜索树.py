#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# [1] 递归算法+中序遍历 --> 52 ms	16.3 MB
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        # 中序遍历二叉搜索树
        self.ans = []
        self.InorderTraversal(root)
        # 利用set集合消除重复项
        return self.ans == sorted(set(self.ans))

    def InorderTraversal(self, root):
        if root.left:
            self.InorderTraversal(root.left)
        self.ans.append(root.val)
        if root.right:
            self.InorderTraversal(root.right)

# [2] 栈+中序遍历 --> 52 ms	15.2 MB
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 中序遍历二叉搜索树
        # 可以不保留ans列表，只记录最后一个遍历到的结点的值，优化内存消耗
        last = float("-inf")
        # 借助栈
        stack = []
        while(root or stack):
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= last:    return False
            last = root.val
            root = root.right
        return True

# [3] 递归算法+上下界 --> 48 ms	15.5 MB
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 递归判断二叉搜索树
        # 递归时添加子数最大、最小值限制
        return self.recursion(root, float('-inf'), float('inf'))
    
    def recursion(self, root, min_subtree, max_subtree):
        if not root:
            return True
        if root.val >= max_subtree or root.val <= min_subtree:
            return False
        return self.recursion(root.left, min_subtree, root.val) and self.recursion(root.right, root.val, max_subtree)

# [4] 栈+上下界 --> 72 ms	15.4 MB
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 借助栈将递归算法转为迭代算法
        stack = [(root, float('-inf'), float('inf'))]
        while(stack):
            root, min_subtree, max_subtree = stack.pop()
            if not root:    continue
            if root.val <= min_subtree or root.val >= max_subtree:
                return False
            stack.append((root.left, min_subtree, root.val))
            stack.append((root.right, root.val, max_subtree))
        return True



# @lc code=end

