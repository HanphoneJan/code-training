#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30204
#
# [51] N 皇后
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 和46.全排列很像
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        queens = [0] * n  # 皇后放在 (row, queens[row])
        used_cols = [False] * n          # 列占用标记
        diag1 = [False] * (n * 2 - 1)    # 主对角线，对角线的索引方式？
        diag2 = [False] * (n * 2 - 1)    # 副对角线

        def dfs(row: int) -> None:
            if row == n:
                # 根据 queens 构建棋盘
                ans.append(['.' * col + 'Q' + '.' * (n - 1 - col) for col in queens])
                return
            # 尝试在当前行的每一列放置皇后
            for col, ok in enumerate(used_cols):
                if not ok and not diag1[row + col] and not diag2[row - col]:
                    queens[row] = col
                    used_cols[col] = diag1[row + col] = diag2[row - col] = True
                    dfs(row + 1)
                    used_cols[col] = diag1[row + col] = diag2[row - col] = False

        dfs(0)
        return ans

# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

