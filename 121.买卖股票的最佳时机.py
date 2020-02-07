#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
# [1] 动态规划（最长子序和思想） --> 通过	64 ms	14.5 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 特判
        n = len(prices)
        if n <= 1:
            return 0
        # 使用diff，将此问题转换为“最长子序和”问题，即求diff数组中的最长子序和
        diff = []
        for i in range(1, n):
            diff.append(prices[i] - prices[i-1])

        if len(diff) <= 1:
            return max(0, diff[0])

        max_Profit = diff[0]
        # 动态规划
        for i in range(1, len(diff)):
            if diff[i-1] > 0:
                diff[i] += diff[i-1]
            max_Profit = max(max_Profit, diff[i])
            
        # 因为利润最小为0，所以取大值
        return max(0, max_Profit)
        
# @lc code=end

