#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
# [1] 两个队列 --> 32 ms	13.4 MB
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.helper = []
        self.topVal = None

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)
        self.topVal = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.data) > 1:
            self.topVal = self.data.pop(0)
            self.helper.append(self.topVal)
        pop = self.data.pop(0)
        self.data, self.helper = self.helper, self.data
        return pop

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.topVal

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.data)==0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

