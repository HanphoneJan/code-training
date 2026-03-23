#
# @lc app=leetcode.cn id=62 lang=python3
# @lcpr version=30204
#
# [62] 不同路径
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from math import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        不同路径 - 组合数学解法

        核心思想：
        从左上角到右下角，需要走 (m-1) 步向下 + (n-1) 步向右 = (m+n-2) 步。
        问题转化为：在这 (m+n-2) 步中选择哪些步向右（或向下），共有多少种选法？

        组合数公式：
        C(m+n-2, n-1) = (m+n-2)! / ((n-1)! * (m-1)!)

        为什么用组合数？
        因为路径只由"何时向右走"决定，一旦确定了向右走的时机，
        向下走的时机也就确定了。

        时间复杂度：O(1) - 直接计算组合数
        空间复杂度：O(1)
        """
        # 选择 n-1 个位置放"右"，其余放"下"
        # 或者选择 m-1 个位置放"下"，两者等价
        return comb(m + n - 2, n - 1)

    def uniquePathsByDP(self, m: int, n: int) -> int:
        """
        动态规划解法

        状态定义：
        dp[i][j] = 从 (0,0) 到达 (i,j) 的不同路径数

        状态转移方程：
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
        （只能从上方或左方到达当前位置）

        边界条件：
        dp[0][j] = 1（第一行只能从左往右走）
        dp[i][0] = 1（第一列只能从上往下走）

        空间优化：
        因为只依赖上一行和当前行的左边，可以用一维数组滚动更新
        """
        # 优化：只用一维数组
        # dp[j] 表示当前行第 j 列的路径数
        dp = [1] * n  # 初始化第一行，所有位置的路径数都是 1

        for i in range(1, m):  # 从第二行开始遍历
            for j in range(1, n):  # 从第二列开始（第一列永远是 1）
                # dp[j] 还没更新，存储的是上一行的值（即 dp[i-1][j]）
                # dp[j-1] 已经更新，存储的是当前行的值（即 dp[i][j-1]）
                dp[j] += dp[j - 1]

        return dp[n - 1]

    def uniquePathsBy2D(self, m: int, n: int) -> int:
        """
        标准二维DP写法，更容易理解
        """
        # dp[i][j] = 到达 (i,j) 的路径数
        dp = [[0] * n for _ in range(m)]

        # 初始化边界：第一行和第一列都只有 1 种走法
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # 填充DP表
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

# @lc code=end



#
# @lcpr case=start
# 3\n7\n
# @lcpr case=end

# @lcpr case=start
# 3\n2\n
# @lcpr case=end

# @lcpr case=start
# 7\n3\n
# @lcpr case=end

# @lcpr case=start
# 3\n3\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        (3, 7, 28),
        (3, 2, 3),
        (7, 3, 28),
        (3, 3, 6),
        (1, 5, 1),
    ]

    for m, n, expected in tests:
        result = sol.uniquePaths(m, n)
        print(f"uniquePaths({m}, {n}) = {result}, expected = {expected}")

