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

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        N 皇后 - 回溯算法（经典问题）

        核心思想：
        在 n×n 的棋盘上放置 n 个皇后，使它们互不攻击。
        皇后可以攻击同一行、同一列、同一对角线上的任意棋子。

        约束条件：
        1. 每行只能放一个皇后（逐行放置）
        2. 每列只能放一个皇后（用 used_cols 标记）
        3. 每条主对角线只能放一个皇后（用 diag1 标记）
        4. 每条副对角线只能放一个皇后（用 diag2 标记）

        对角线索引技巧：
        - 主对角线（左上到右下）：row - col 是常数，但可能为负数
          所以用 row - col + (n-1) 作为索引，范围 [0, 2n-2]
        - 副对角线（右上到左下）：row + col 是常数
          所以用 row + col 作为索引，范围 [0, 2n-2]

        时间复杂度：O(n!) - 第一行 n 种选择，第二行最多 n-1 种...
        空间复杂度：O(n) - 递归深度和标记数组
        """
        ans = []
        queens = [0] * n  # queens[row] = col，表示第 row 行第 col 列放置皇后

        # 冲突标记数组
        used_cols = [False] * n          # 列占用标记
        diag1 = [False] * (n * 2 - 1)    # 主对角线（row - col + n - 1）
        diag2 = [False] * (n * 2 - 1)    # 副对角线（row + col）

        def dfs(row: int) -> None:
            """
            在第 row 行放置皇后
            参数 row: 当前处理的行号（从0开始）
            """
            # 结束条件：所有行都放置完毕
            if row == n:
                # 根据 queens 数组构建棋盘表示
                # 每行字符串：'.' * col + 'Q' + '.' * (n - 1 - col)
                board = []
                for col in queens:
                    board.append('.' * col + 'Q' + '.' * (n - 1 - col))
                ans.append(board)
                return

            # 尝试在当前行的每一列放置皇后
            for col in range(n):
                # 检查冲突：
                # 1. used_cols[col]: 该列是否已有皇后
                # 2. diag1[row + col]: 副对角线是否已有皇后
                # 3. diag2[row - col + n - 1]: 主对角线是否已有皇后
                d1 = row + col           # 副对角线索引
                d2 = row - col + n - 1   # 主对角线索引

                if not used_cols[col] and not diag1[d1] and not diag2[d2]:
                    # 做选择：在第 row 行第 col 列放置皇后
                    queens[row] = col
                    used_cols[col] = diag1[d1] = diag2[d2] = True

                    # 递归处理下一行
                    dfs(row + 1)

                    # 撤销选择：恢复现场（回溯）
                    used_cols[col] = diag1[d1] = diag2[d2] = False

        dfs(0)
        return ans

    def solveNQueensCount(self, n: int) -> int:
        """
        只返回解的个数，不需要输出所有解
        """
        count = 0
        used_cols = [False] * n
        diag1 = [False] * (n * 2 - 1)
        diag2 = [False] * (n * 2 - 1)

        def dfs(row: int) -> None:
            nonlocal count
            if row == n:
                count += 1
                return

            for col in range(n):
                d1, d2 = row + col, row - col + n - 1
                if not used_cols[col] and not diag1[d1] and not diag2[d2]:
                    used_cols[col] = diag1[d1] = diag2[d2] = True
                    dfs(row + 1)
                    used_cols[col] = diag1[d1] = diag2[d2] = False

        dfs(0)
        return count

# @lc code=end



#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        4,
        1,
        8,
    ]

    for n in tests:
        result = sol.solveNQueens(n)
        print(f"solveNQueens({n}) = {len(result)} solutions")

