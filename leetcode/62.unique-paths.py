#
# @lc app=leetcode.cn id=62 lang=python3
# @lcpr version=30204
#
# [62] 不同路径
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# DP模拟法或者用排列组合知识直接得到最终公式

# def factorial(n):
#     if n < 0:
#         raise ValueError("阶乘不能为负数")
#     result = 1
#     for i in range(2, n+1):
#         result *= i
#     return result
from math import factorial,comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # return comb(m + n - 2, n - 1)
        return factorial(m+n-2)//(factorial(m-1)*factorial(n-1))

    # f(i,j)=f(i−1,j)+f(i,j−1)
    def uniquePathsByDP(self, m: int, n: int) -> int:
        f = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                f[j] += f[j - 1]
        return f[n - 1]

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

