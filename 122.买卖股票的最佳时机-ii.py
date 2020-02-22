#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
# [1] 动态规划（最长子序和思想） --> 72 ms	14.7 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        # diff表示第i天买入，第i+1天卖出，获得的利润
        diff = [prices[i+1]-prices[i] for i in range(n-1)]
        if len(diff) == 1:
            return max(0, diff[0])
        # 动态规划 令dp[i]表示第i天之前，能获得的最大利润
        # dp[i] = dp[i-1] + diff[i] if diff[i] > 0 else dp[i-1]
        diff[0] = max(0, diff[0])
        for i in range(1, n-1):
            if diff[i] > 0:
                diff[i] += diff[i-1]
            else:
                diff[i] = diff[i-1]
        return diff[n-2]

# [2] 峰谷法 --> 64 ms	14.6 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        # 峰谷法
        i = 0
        profit = 0
        while i < n-1:
            # 先寻找波谷
            while i < n-1 and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]
            # 在寻找波峰
            while i < n-1 and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]
            profit += peak - valley
        return profit

# [3] 贪心算法 --> 116 ms	14.6 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        # 贪心算法
        max_profit = 0
        for i in range(n-1):
            profit = prices[i+1] - prices[i]
            if profit > 0:
                max_profit += profit
        return max_profit

# @lc code=end

