#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
# 二分查找有序部分 --> 168 ms	29 MB
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1

        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] == target:
                return mid
            # 如果前半部分有序，则在前半部分查找；否则，后半部分查找
            if nums[left] <= nums[mid]:
                # 如果target在前半部分，那么right=mid-1
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 如果target在后半部分，那么left=mid+1
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        
# @lc code=end

