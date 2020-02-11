#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
'''
# [1] 暴力法 --> 188 ms	13.1 MB
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 暴力法
        # 扫描行、列
        for i in range(9):
            # 记录横向数字
            hasmap1 = {}
            # 记录纵向数字
            hasmap2 = {}
            for j in range(9):
                # 横向
                if board[i][j] != '.':
                    if board[i][j] in hasmap1:
                        return False
                    hasmap1[board[i][j]] = 1
                # 纵向
                if board[j][i] != '.':
                    if board[j][i] in hasmap2:
                        return False
                    hasmap2[board[j][i]] = 1
        # 扫描3x3宫
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                hasmap3 = {}
                for m in range(3):
                    for n in range(3):
                        if board[i+m][j+n] != '.':
                            if board[i+m][j+n] in hasmap3:
                                return False
                            hasmap3[board[i+m][j+n]] = 1
        return True

# [2] 哈希表 --> 124 ms	13.2 MB
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 使用一张哈希表，记录每个数字出现的坐标
        hasmap = {str(x):[] for x in range(1,10)}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                        hasmap[board[i][j]].append([i, j])
        
        # 遍历哈希表，根据坐标判断是否为有效数独
        for key, index in hasmap.items():
            n = len(index)
            if n <= 1:
                continue
            else:
                # 坐标两两比较
                for i in range(n-1):
                    for j in range(i+1,n):
                        # 是否在同一行、同一列
                        if index[i][0] == index[j][0] or index[i][1] == index[j][1]:
                            return False
                        # 是否在同一个3x3宫内
                        if index[i][0]//3 == index[j][0]//3 and index[i][1]//3 == index[j][1]//3:
                            return False
        return True
'''
# [3] 一次迭代法 --> 100 ms	12.8 MB
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 一次迭代法
        rows = [{} for _ in range(9)]
        columns = [{} for _ in range(9)]
        box = [{} for _ in range(9)]
        # 一行3个box，box_index = i//3 * 3 + j//3
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    box_index = i//3 * 3 + j//3
                    if num in rows[i] or num in columns[j] or num in box[box_index]:
                        return False
                    rows[i][num] = 1
                    columns[j][num] = 1
                    box[box_index][num] = 1
        return True

# @lc code=end

