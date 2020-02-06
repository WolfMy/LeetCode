#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
# [1] 合并排序 --> 通过	128 ms	13.2 MB
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        nums.extend(nums1)
        nums.extend(nums2)
        nums.sort()
        n = len(nums)
        if n % 2 == 0:
            median = (nums[int(n/2)-1] + nums[int(n/2)]) / 2
        else:
            median = nums[n//2]
        return 1.0 * median
        
# @lc code=end

