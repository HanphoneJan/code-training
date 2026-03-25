#
# @lc app=leetcode.cn id=64 lang=python3
# @lcpr version=30204
#
# [64] 最小路径和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    """
    最小路径和 - 动态规划

    核心思想：
    从左上角到右下角，每次只能向右或向下移动，求路径和最小值。

    状态定义：
    dp[i][j] = 从 (0,0) 到达 (i,j) 的最小路径和

    状态转移方程：
    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    （只能从上方或左方到达当前位置，选择路径和较小的那个）

    边界条件：
    - dp[0][0] = grid[0][0]
    - 第一行：只能从左边来，dp[0][j] = dp[0][j-1] + grid[0][j]
    - 第一列：只能从上面来，dp[i][0] = dp[i-1][0] + grid[i][0]

    时间复杂度：O(m * n)
    空间复杂度：O(m * n)，可以优化到 O(n)
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, columns = len(grid), len(grid[0])

        # dp[i][j] = 到达 (i,j) 的最小路径和
        dp = [[0] * columns for _ in range(rows)]
        dp[0][0] = grid[0][0]

        # 初始化第一列：只能从上方来
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # 初始化第一行：只能从左边来
        for j in range(1, columns):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # 填充 DP 表
        for i in range(1, rows):
            for j in range(1, columns):
                # 从上方或左方选择较小的路径和，加上当前格子的值
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[rows - 1][columns - 1]


# ========== 示例推演：grid = [[1,3,1],[1,5,1],[4,2,1]] ==========
#
# dp[0][0] = 1
# dp[1][0] = 1+1 = 2, dp[2][0] = 2+4 = 6
# dp[0][1] = 1+3 = 4, dp[0][2] = 4+1 = 5
#
# dp[1][1] = min(dp[0][1], dp[1][0]) + 5 = min(4, 2) + 5 = 7
# dp[1][2] = min(dp[0][2], dp[1][1]) + 1 = min(5, 7) + 1 = 6
# dp[2][1] = min(dp[1][1], dp[2][0]) + 2 = min(7, 6) + 2 = 8
# dp[2][2] = min(dp[1][2], dp[2][1]) + 1 = min(6, 8) + 1 = 7
#
# 结果：7（路径：1→1→5→1→1 或 1→3→1→1→1，都是7）
# @lc code=end



#
# @lcpr case=start
# [[1,3,1],[1,5,1],[4,2,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3],[4,5,6]]\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 2, 3], [4, 5, 6]], 12),
        ([[1]], 1),
        ([[1, 2], [1, 1]], 3),
    ]

    for grid, expected in tests:
        result = sol.minPathSum(grid)
        print(f"minPathSum({grid}) = {result}, expected = {expected}")
