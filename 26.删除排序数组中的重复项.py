#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
'''
# [1] 复制+遍历 --> 通过	1164 ms	14.8 MB
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_copy = nums.copy()
        for i in range(1, len(nums_copy)):
            if nums_copy[i] == nums_copy[i-1]:
                nums.remove(nums_copy[i])
        return len(nums)
'''

# [2] 快慢指针 --> 通过	148 ms	14.9 MB
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 快慢指针
        i = 0
        for j in range(1, len(nums)):
            # 如果j指向的值与i指向的值不同，那么把j的值移到i+1位置；否则即为重复值，跳过。
            if nums[i] != nums[j]:
                # 且只有当 j - i > 1 时，才进行复制。  -->  优化执行时间为112 ms	14.9 MB
                if j - i > 1:
                    nums[i+1] = nums[j]
                i += 1
        # i最终指向不重复列表尾部
        return i+1
        
# @lc code=end

