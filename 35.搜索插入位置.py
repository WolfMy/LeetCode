#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
# 二分查找 --> 116 ms	29.9 MB
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return 0

        if nums[n-1] < target:
            return n
        if nums[0] > target:
            return 0

        # 二分查找
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

# @lc code=end

