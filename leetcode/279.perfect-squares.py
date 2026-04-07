#
# @lc app=leetcode.cn id=279 lang=python3
# @lcpr version=30204
#
# [279] 完全平方数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 居然是动态规划！经典记忆化搜索/递推
# 状态转移方程是什么？
from functools import cache
from math import inf,isqrt

# 写在外面，多个测试数据之间可以共享，减少计算量
@cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
def dfs(i: int, j: int) -> int:
    if i == 0:
        return inf if j else 0
    if j < i * i:
        return dfs(i - 1, j)  # 只能不选
    return min(dfs(i - 1, j), dfs(i, j - i * i) + 1)  # 不选 vs 选

class Solution:
    def numSquares(self, n: int) -> int:
        return dfs(isqrt(n), n)


# N = 10000
# f = [0] + [inf] * N
# for i in range(1, isqrt(N) + 1):
#     for j in range(i * i, N + 1):
#         f[j] = min(f[j], f[j - i * i] + 1)  # 不选 vs 选

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

