#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30204
#
# [279] 完全平方数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache
from math import inf, isqrt


# 写在外面，多个测试数据之间可以共享，减少计算量
@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
def dfs(i: int, j: int) -> int:
    """
    记忆化搜索：从前 i 个完全平方数中选择，组成和为 j 的最少个数
    i: 考虑前 i 个完全平方数 (1^2, 2^2, ..., i^2)
    j: 目标和
    返回: 最少需要的完全平方数个数
    """
    if i == 0:
        return inf if j else 0
    if j < i * i:
        # 当前完全平方数 i^2 太大，只能不选
        return dfs(i - 1, j)
    # 状态转移：不选 i^2 vs 选 i^2（选的话可以继续选，所以是 dfs(i, ...)）
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)


class Solution:
    """
    279. 完全平方数 - 动态规划/记忆化搜索

    问题本质：
    给定 n，求最少的完全平方数个数，使得它们的和等于 n。
    这是一个经典的"完全背包"问题。

    解法一：记忆化搜索（自顶向下）
    - 定义 dfs(i, j)：从前 i 个完全平方数中选，组成和为 j 的最少个数
    - 状态转移：min(不选 i^2, 选 i^2 + 1)
    - 使用 @cache 避免重复计算

    解法二：递推/完全背包（自底向上）
    - f[j] 表示组成和为 j 的最少完全平方数个数
    - 初始化：f[0] = 0, f[1..n] = inf
    - 转移：f[j] = min(f[j], f[j - i*i] + 1) 对于所有 i*i <= j

    数学定理（拉格朗日四平方和定理）：
    每个正整数都可以表示为最多 4 个完全平方数的和。
    因此答案只可能是 1, 2, 3, 4。

    时间复杂度: O(n * sqrt(n)) - 对于每个数，考虑所有可能的完全平方数
    空间复杂度: O(n) - 记忆化/DP 数组的空间
    """

    def numSquares(self, n: int) -> int:
        """使用记忆化搜索求解"""
        return dfs(isqrt(n), n)


# 解法二：完全背包递推（预处理版本）
# N = 10000
# f = [0] + [inf] * N
# for i in range(1, isqrt(N) + 1):
#     for j in range(i * i, N + 1):
#         f[j] = min(f[j], f[j - i * i] + 1)  # 不选 vs 选
#
# class Solution:
#     def numSquares(self, n: int) -> int:
#         return f[n]


# @lc code=end



#
# @lcpr case=start
# 12\n
# @lcpr case=end

# @lcpr case=start
# 13\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例: (n, expected)
    tests = [
        (12, 3),   # 12 = 4 + 4 + 4
        (13, 2),   # 13 = 4 + 9
        (1, 1),    # 1 = 1
        (2, 2),    # 2 = 1 + 1
        (3, 3),    # 3 = 1 + 1 + 1
        (4, 1),    # 4 = 4
        (100, 1),  # 100 = 100
    ]

    for n, expected in tests:
        result = sol.numSquares(n)
        print(f"n={n}, result={result}, expected={expected}, {'✓ PASS' if result == expected else '✗ FAIL'}")
