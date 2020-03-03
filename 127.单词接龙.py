#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start

# [1] 图论+BFS --> 124 ms	17.2 MB
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not wordList:
            return 0
        # 预处理：将字典里的单次，如hit拆分为 *it、h*t、hi* 三种形式
        n = len(beginWord)
        all_combinations = defaultdict(list)
        for word in wordList:
            for i in range(n):
                wildcard = word[:i] + '*' + word[i+1:]
                all_combinations[wildcard].append(word)
        # 存储已访问过的单词
        visited = {beginWord:True}
        queue = [(beginWord, 1)]
        while queue:
            nextword, level = queue.pop(0)
            # 尝试这个单词所有的通配形式
            for i in range(n):
                wildcard = nextword[:i] + '*' + nextword[i+1:]
                if wildcard in all_combinations:
                    # 若通配形式存在，那么把此形式的所有单词放进队列
                    for word in all_combinations[wildcard]:
                        if word == endWord:
                            return (level + 1)
                        # 进队列的前提是这个单词未被访问过
                        if word not in visited:
                            queue.append((word, level+1))
                            visited[word] = True
        return 0

# [2] 图论+双向BFS --> 84 ms	17.3 MB
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not wordList:
            return 0
        # 预处理：将字典里的单次，如hit拆分为 *it、h*t、hi* 三种形式
        self.n = len(beginWord)
        self.all_combinations = defaultdict(list)
        for word in wordList:
            for i in range(self.n):
                wildcard = word[:i] + '*' + word[i+1:]
                self.all_combinations[wildcard].append(word)
        # 存储从beginWord访问过的单词和层数
        begin_visited = {beginWord:1}
        begin_queue = [(beginWord, 1)]
        # 存储从endWord访问过的单词和层数
        end_visited = {endWord:1}
        end_queue = [(endWord, 1)]
        while begin_queue and end_queue:
            ans = self.visitWordNode(begin_queue, begin_visited, end_visited)
            if ans: return ans
            ans = self.visitWordNode(end_queue, end_visited, begin_visited)
            if ans: return ans
        return 0

    def visitWordNode(self, queue, visited, another_visited):
        nextword, level = queue.pop(0)
        # 尝试这个单词所有的通配形式
        for i in range(self.n):
            wildcard = nextword[:i] + '*' + nextword[i+1:]
            if wildcard in self.all_combinations:
                # 若通配形式存在，那么把此形式的所有单词放进队列
                for word in self.all_combinations[wildcard]:
                    # 若与另一方向相遇，那么总长度为当前level+另一方向的level
                    if word in another_visited:
                        return level + another_visited[word]
                    # 进队列的前提是这个单词未被访问过
                    if word not in visited:
                        queue.append((word, level+1))
                        visited[word] = level + 1

