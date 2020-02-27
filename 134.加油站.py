#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#

# @lc code=start
# [1] 暴力法 --> 5196 ms	14.3 MB
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 暴力法
        n = len(gas)
        for i in range(n):
            # 从第i个加油站出发，能否回到起点
            j = i
            curGas = 0
            while True:
                curGas = curGas + gas[j] - cost[j]
                if curGas < 0:
                    break
                j = (j+1)%n
                if j == i:
                    return i
        return -1

# [2] 一次迭代法 --> 60 ms	14.6 MB
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # 计算净油耗
        netCost = [gas[i]-cost[i] for i in range(n)]
        if sum(netCost) < 0:
            return -1

        curGas = 0
        start = -1
        for i in range(n):
            # 如果起点为-1且当前位置净油耗大于0，那么尝试将当前位置作为起点
            if start == -1 and netCost[i] >= 0:
                start = i
            # 记录出发后的油量，当油量小于0时，更新起点为-1并重置油量
            if start != -1:
                curGas += netCost[i]
                if curGas < 0:
                    start = -1
                    curGas = 0
        return start

# @lc code=end

