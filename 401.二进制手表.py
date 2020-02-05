#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
# 回溯法 --> 通过 40 ms 13.2 MB
class Solution:
    def __init__(self):
        self.nums = [1,2,4,8,1,2,4,8,16,32]
        self.visited = [0 for _ in range(len(self.nums))]
        self.result_all = []

    def readBinaryWatch(self, num: int) -> List[str]:
        self.dfs(num, 0, 0)
        return self.result_all

    def dfs(self, num, step, start):
        # 回溯结构
        if(num == step):
            self.result_all.append(self.handle_date(self.visited))
            return
        
        for i in range(start, len(self.nums)):
            self.visited[i] = 1
            if not self.check_date(self.visited):
                # 如果选择此i后，时间不合法，那么取消选择此i
                self.visited[i] = 0
                continue
            # 继续选择
            self.dfs(num, step+1, i+1)
            # 回溯
            self.visited[i] = 0

    def cal_date(self, visited):
        # 计算小时和分钟总和
        sum_h = 0
        sum_m = 0
        for i in range(4):
            if visited[i] == 1:
                sum_h += self.nums[i]
        for j in range(4,len(self.nums)):
            if visited[j] == 1:
                sum_m += self.nums[j]
        return sum_h, sum_m

    def check_date(self, visited):
        # 检查时间是否合法：小时（0-11）and 分钟（0-59）
        sum_h, sum_m = self.cal_date(visited)
        return sum_h <= 11 and sum_m <= 59

    def handle_date(self, visited):
        # 规格化时间的函数
        sum_h, sum_m = self.cal_date(visited)
        h = str(sum_h)
        m = '0'+str(sum_m) if sum_m < 10 else str(sum_m)
        return h + ':' + m
        
# @lc code=end

