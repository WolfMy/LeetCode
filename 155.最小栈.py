#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
# [1] 同步辅助栈 --> 76 ms	16.5 MB
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            # 否则辅助栈再次入栈最小值
            self.helper.append(self.helper[-1])
        
    def pop(self) -> None:
        self.data.pop()
        self.helper.pop()
        
    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.helper[-1]

# [2] 不同步辅助栈 --> 128 ms	16.6 MB
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x: int) -> None:
        self.data.append(x)
        # 只有当x小于辅助栈顶元素，x才入辅助栈
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self) -> None:
        pop = self.data.pop()
        # 只有当x等于辅助栈顶元素，辅助栈才出栈
        if pop == self.helper[-1]:
            self.helper.pop()
        
    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.helper[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

