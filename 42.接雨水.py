#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
# [1] 双指针 --> 60 ms	13.7 MB
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        # 双指针
        left = 0
        right = n - 1
        # 分别记录左右目前最高高度
        leftHeight = height[left]
        rightHeight = height[right]
        ans = 0
        while left < right:
            # 若遇到比目前高度小的或相等的，那么水量+=高度差
            # 若遇到比目前高度大的，那么更新目前高度
            if height[left] <= height[right]:
                if height[left] > leftHeight:
                    leftHeight = height[left]
                else:
                    ans += leftHeight - height[left]
                left += 1
            else:
                if height[right] > rightHeight:
                    rightHeight = height[right]
                else:
                    ans += rightHeight - height[right]
                right -= 1
        return ans

# [2] 栈 --> 48 ms	14 MB
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 1:
            return 0
        current = 0
        stack = []
        ans = 0
        while current < n:
            # 如果栈为空，那么入栈当前高度的下标，指针后移
            # 如果栈不为空：
            #   若当前高度小于栈顶指向的高度，入栈当前高度的下标
            #   否则，边出栈边计算积水量
            while stack and height[current] > height[stack[-1]]:
                h = stack.pop()
                if not stack:
                    break
                distance = current - stack[-1] - 1
                bounedHeight = min(height[current], height[stack[-1]]) - height[h]
                ans += distance * bounedHeight
            stack.append(current)
            current += 1
        return ans
# @lc code=end

