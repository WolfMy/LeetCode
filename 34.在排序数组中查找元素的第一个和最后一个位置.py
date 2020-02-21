#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
# [1] 二分查找 --> 164 ms	29.9 MB
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        # 二分查找target，找到target后,分别往左、往右查找第一个和最后一个位置
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res = []
                # 往左查找第一个位置
                first = mid
                while first >= 1 and nums[first-1] == target:
                    first -= 1
                res.append(first)
                # 往右查找最后一个位置
                last = mid
                while last <= n-2 and nums[last+1] == target:
                    last += 1
                res.append(last)
                return res
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]
# [2] 二分查找的变形 --> 176 ms	29.5 MB
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        return [self.left_bound(nums, target), self.right_bound(nums, target)]
        
    def left_bound(self, nums, target):
        # 查找左边界，找到target后，right左移一个单位
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if left <= len(nums)-1 and nums[left] == target:
            return left
        else:
            return -1

    def right_bound(self, nums, target):
        # 查找右边界，找到target后，left右移一个单位
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if right >= 0 and nums[right] == target:
            return right
        else:
            return -1

# @lc code=end

