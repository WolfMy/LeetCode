#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# [1] BFS+双端队列 --> 40 ms	13.6 MB
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # None为分隔符
        queue = [root, None]
        # level_res是一个双端队列，存储一层的节点遍历结果
        level_res = deque()
        # 是否为从左往右遍历
        is_order_left = True
        res = []
        while queue:
            root = queue.pop(0)

            if root:
                if is_order_left:
                    # 添加到队列首部
                    level_res.append(root.val)
                else:
                    level_res.appendleft(root.val)

                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            else:
                # 若遇到分隔符，表示本层遍历完成
                res.append(list(level_res))
                level_res = deque()
                is_order_left = not is_order_left
                # 如果队列里还有元素，那么添加分隔符
                if queue:
                    queue.append(None)
        return res

# [2] DFS+双端队列 --> 40 ms	13.6 MB
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, 0)]
        res = []
        # DFS
        while stack:
            root, level = stack.pop()
            if len(res) == level:
                res.append(deque())

            if level%2 == 0:
                res[level].appendleft(root.val)
            else:
                res[level].append(root.val)

            if root.left:
                stack.append((root.left, level+1))
            if root.right:
                stack.append((root.right, level+1))
        res = [list(deque_) for deque_ in res]
        return res
        
# @lc code=end

