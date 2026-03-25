#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30204
#
# [70] 爬楼梯
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    爬楼梯 - 动态规划

    核心思想：
    爬到第 n 阶楼梯的方法数 = 爬到第 n-1 阶的方法数 + 爬到第 n-2 阶的方法数
    因为最后一步可以跨1阶或2阶。

    状态转移方程：
    f(n) = f(n-1) + f(n-2)

    初始条件：
    f(0) = 1（地面有一种方法：不动）
    f(1) = 1（只有1阶，只有一种方法）

    空间优化：
    只需要保存前两个状态，用滚动数组将空间复杂度优化到 O(1)

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    def climbStairs(self, n: int) -> int:
        # f0 表示 f(n-2)，f1 表示 f(n-1)
        f1 = f0 = 1
        for i in range(2, n + 1):
            new_f = f1 + f0  # f(n) = f(n-1) + f(n-2)
            f0 = f1          # 更新 f(n-2) 为 f(n-1)
            f1 = new_f       # 更新 f(n-1) 为 f(n)
        return f1


# ========== 示例推演：n = 3 ==========
#
# 初始：f0 = 1 (f(0)), f1 = 1 (f(1))
#
# i=2: new_f = 1 + 1 = 2 (f(2))
#      f0 = 1, f1 = 2
#
# i=3: new_f = 2 + 1 = 3 (f(3))
#      f0 = 2, f1 = 3
#
# 返回 3
# 三种方法：1+1+1, 1+2, 2+1
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        (2, 2),
        (3, 3),
        (1, 1),
        (4, 5),
        (5, 8),
    ]

    for n, expected in tests:
        result = sol.climbStairs(n)
        print(f"climbStairs({n}) = {result}, expected = {expected}")
