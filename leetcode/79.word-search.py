#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30204
#
# [79] 单词搜索
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 难得我自己写出来，虽然靠了DeepSeek帮我debug
from typing import List
from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 优化一：字母频率预检
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word):
            return False
        
        # 优化二：首尾字母优化，从出现次数更少的字母开始搜索
        if cnt[word[-1]] < cnt[word[0]]:
            word = word[::-1]
        
        m, n = len(board), len(board[0])
        
        def dfs(i: int, j: int, k: int) -> bool:  # 优化三：使用索引标记匹配到第几个字符，不需要创建新字符串
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''  # 标记已访问
            # 四个方向，简洁展开
            for x, y in (i, j-1), (i, j+1), (i-1, j), (i+1, j):
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k+1):
                    return True
            board[i][j] = word[k]  # 恢复现场
            return False
        
        # 优化四：使用 any() + 生成器，简洁且短路
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
# @lc code=end



#
# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]\n"ABCB"\n
# @lcpr case=end

#

