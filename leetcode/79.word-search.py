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
from collections import Counter

class Solution:
    """
    单词搜索 - 回溯算法（DFS）

    核心思想：
    从矩阵的每个位置出发，使用 DFS 搜索是否存在一条路径能组成目标单词。

    回溯的关键：
    1. 标记已访问：将访问过的格子标记为空字符串，避免重复使用
    2. 恢复现场：回溯时将格子恢复原值，供其他路径使用
    3. 四个方向搜索：上下左右

    优化技巧：
    1. 字母频率预检：如果 board 中某字母数量少于 word，直接返回 False
    2. 首尾优化：从出现次数较少的字母端开始搜索
    3. 使用索引 k 标记匹配进度，避免创建新字符串

    时间复杂度：O(m * n * 3^L)，L 是单词长度，每个格子有3个方向（来的方向不回头）
    空间复杂度：O(L)，递归栈深度
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 优化一：字母频率预检
        cnt = Counter(c for row in board for c in row)
        if not cnt >= Counter(word):
            return False

        # 优化二：首尾字母优化，从出现次数更少的字母开始搜索
        if cnt[word[-1]] < cnt[word[0]]:
            word = word[::-1]

        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, k: int) -> bool:
            """
            从 (i,j) 开始匹配 word[k:]
            k: 当前匹配到 word 的第 k 个字符
            """
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            # 标记已访问
            board[i][j] = ''

            # 四个方向搜索
            for x, y in (i, j-1), (i, j+1), (i-1, j), (i+1, j):
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k+1):
                    return True

            # 恢复现场（回溯）
            board[i][j] = word[k]
            return False

        # 从每个格子开始尝试
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))


# ========== 示例推演：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED" ==========
#
# 从 (0,0) 'A' 开始：
#   dfs(0,0,0): 'A'=='A' ✓，标记为''，搜索邻居
#     dfs(0,1,1): 'B'=='B' ✓，标记为''
#       dfs(0,2,2): 'C'=='C' ✓，标记为''
#         dfs(0,3,3): 'E'!='C' ✗
#         dfs(1,2,3): 'C'=='C' ✓，标记为''
#           dfs(1,1,4): 'F'!='E' ✗
#           dfs(2,2,4): 'E'=='E' ✓
#             dfs(2,1,5): 'D'=='D' ✓，k=5==len(word)-1，返回 True
#
# 结果：True
# @lc code=end



#
# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
"ABCCED"

# @lcpr case=end

# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
"SEE"

# @lcpr case=end

# @lcpr case=start
# [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
"ABCB"

# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
        ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False),
    ]

    for board, word, expected in tests:
        result = sol.exist(board, word)
        print(f"exist({board}, '{word}') = {result}, expected = {expected}")
