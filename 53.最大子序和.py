#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start
# [1] 动态规划 --> 通过	80 ms	13.9 MB
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 特判：如果只有1个元素，则返回自己
        n = len(nums)
        if n <= 1:
            return sum(nums)
        # dp存储的是：前i个数中，具有最大和的连续子数组，的最大和
        # 初始化为自身，这里可以直接在nums上修改
        # dp = nums.copy() 
        maxSub = nums[0]
        # 自底向上
        for i in range(1, n):
            # 如果dp[i-1]大于0，那么dp[i-1]+nums[i]肯定大于dp[i]
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            maxSub = max(maxSub, nums[i])
        return maxSub

