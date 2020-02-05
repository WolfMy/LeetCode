#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
# 回溯法 --> 通过 64 ms 13.5 MB
class Solution:
    def __init__(self):
        self.result = []

    def letterCasePermutation(self, S: str) -> List[str]:
        arr = list(S)
        self.backtracing(arr, 0)
        return self.result

    def backtracing(self, arr, start):
        if start == len(arr):
            self.result.append(''.join(arr))
            return
        # 把自身递归
        self.backtracing(arr, start+1)
        # 若是字母，则切换大小写后递归
        if arr[start].isalpha():
            arr[start] =  arr[start].lower() if arr[start].isupper() else arr[start].upper()
            self.backtracing(arr, start+1)
        
# @lc code=end

