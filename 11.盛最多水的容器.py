#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
'''
# [1] 暴力法 --> 超出时间限制
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                max_area = max(max_area, (j-i) * min(height[i],height[j]))
        return max_area
'''
# [2] 双指针法 --> 通过	160 ms	27.1 MB
class Solution:
    def __init__(self):
        self.max_area = 0

    def maxArea(self, height: List[int]) -> int:
        # 双指针
        i = 0
        j = len(height) - 1
        self.recursive(height, i, j)
        return self.max_area
    
    def recursive(self, height, i, j):
        # 如果左右指针相遇，则结束递归
        if i == j:
            return
        
        # 计算当前左右指针围成的面积，更新最大面积
        self.max_area = max(self.max_area, (j-i)*min(height[i],height[j]))

        if height[i] >= height[j]:
            # 如果左指针值>=右指针值，那么右指针左移
            self.recursive(height, i, j-1)
        else:
            # 否则，左指针右移
            self.recursive(height, i+1, j)
        
# @lc code=end

