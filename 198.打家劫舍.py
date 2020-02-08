#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
'''
# [1] 动态规划（自顶向下，记忆化） --> 通过	36 ms	13.1 MB
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 特判
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        
        # 动态规划：dp[i]表示从前i个房屋中能偷窃到的最大现金 (i <= n-1)
        # 若偷窃第i间房，则 现金 = dp[i-2] + nums[i]
        # 若不偷窃第i间房，则 现金 = dp[i-1]
        # 于是最大现金则为 max(dp[i-2]+nums[i], dp[i-1])
        # 使用哈希表实现记忆化
        self.hasmap = {0:nums[0]}
        max_money = max(self.rob_recursion(nums, n-3) + nums[n-1], 
                        self.rob_recursion(nums, n-2))
        return max_money

    def rob_recursion(self, nums, i):
        if i < 0:
            return 0
        if i in self.hasmap:
            return self.hasmap[i]
        else:
            self.hasmap[i] = max(self.rob_recursion(nums, i-2) + nums[i],
                            self.rob_recursion(nums, i-1))
            return self.hasmap[i]
'''
# [2] 动态规划（自底向上） --> 通过	32 ms	13.1 MB
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # 特判
        if n == 0:
            return 0
        if n <= 2:
            return max(nums)
        
        # 动态规划：dp[i]表示从前i个房屋中能偷窃到的最大现金 (i <= n-1)
        # 若偷窃第i间房，则 现金 = dp[i-2] + nums[i]
        # 若不偷窃第i间房，则 现金 = dp[i-1]
        # 于是最大现金则为 max(dp[i-2]+nums[i], dp[i-1])
        # 初始化: dp[0] = nums[0]
        #        dp[1] = max(nums[1], dp[0])
        nums[1] = max(nums[1], nums[0])
        # 自底向上
        for i in range(2, n):
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
        return max(nums)


        
        
        



        
# @lc code=end

