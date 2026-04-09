#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30204
#
# [322] 零钱兑换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from math import inf
from functools import cache


class Solution:
    """
    322. 零钱兑换 - 完全背包问题

    问题本质：
    给定不同面额的硬币 coins 和总金额 amount，求组成该金额所需的最少硬币个数。
    每个硬币可以无限次使用，这是一个经典的"完全背包"问题。

    解法一：记忆化搜索（自顶向下）
    - 定义 dfs(i, c)：从前 i 种硬币中选，组成金额 c 的最少硬币数
    - 状态转移：min(不选 coin[i], 选 coin[i] + 1)
    - 使用 @cache 避免重复计算
    - 缺点：递归有额外开销，缓存访问不连续

    解法二：动态规划/完全背包（自底向上）
    - f[c] 表示组成金额 c 所需的最少硬币数
    - 初始化：f[0] = 0, f[1..amount] = inf
    - 转移：对于每种硬币，遍历所有可以组成的金额
            f[cur] = min(f[cur], f[cur - coin] + 1)
    - 外层循环硬币，内层循环金额（完全背包的标准写法）

    为什么外层循环是硬币？
    - 确保每种硬币可以被重复使用
    - 如果外层是金额，内层是硬币，会超时（变成排列问题）

    时间复杂度: O(n * amount) - n 为硬币种类数
    空间复杂度: O(amount) - DP 数组空间
    """

    # 解法一：记忆化搜索
    def coinChange_memo(self, coins: List[int], amount: int) -> int:
        """
        记忆化搜索解法
        dfs(i, c) 表示从前 i 种硬币中选，组成金额 c 的最少硬币数
        """
        @cache
        def dfs(i: int, c: int) -> int:
            if i < 0:
                # 没有硬币可选，只有金额为 0 时才可行
                return 0 if c == 0 else inf
            if c < coins[i]:
                # 当前硬币面值太大，只能不选
                return dfs(i - 1, c)
            # 状态转移：不选当前硬币 vs 选当前硬币（可以继续选，所以是 dfs(i, ...)）
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

        ans = dfs(len(coins) - 1, amount)
        return ans if ans < inf else -1

    # 解法二：完全背包（最优解法）
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        完全背包动态规划解法
        f[c] 表示组成金额 c 所需的最少硬币数
        """
        # 初始化：f[0] = 0（组成金额 0 需要 0 个硬币）
        # 其余初始化为无穷大，表示暂时不可达
        f = [0] + [inf] * amount

        # 外层循环：每种硬币
        for coin in coins:
            # 内层循环：从 coin 到 amount
            # 从 coin 开始是因为更小的金额无法使用该硬币
            for cur in range(coin, amount + 1):
                # 状态转移：不使用当前硬币 vs 使用当前硬币（数量 +1）
                f[cur] = min(f[cur], f[cur - coin] + 1)

        ans = f[amount]
        return ans if ans < inf else -1



#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例: (coins, amount, expected)
    tests = [
        ([1, 2, 5], 11, 3),      # 11 = 5 + 5 + 1
        ([2], 3, -1),             # 无法用 2 组成 3
        ([1], 0, 0),              # 组成金额 0 需要 0 个硬币
        ([1], 1, 1),
        ([1], 2, 2),
        ([186, 419, 83, 408], 6249, 20),  # 大金额测试
    ]

    print("Testing DP solution:")
    for coins, amount, expected in tests:
        result = sol.coinChange(coins, amount)
        print(f"coins={coins}, amount={amount}, result={result}, expected={expected}, {'✓ PASS' if result == expected else '✗ FAIL'}")

    print("\nTesting Memoization solution:")
    for coins, amount, expected in tests:
        result = sol.coinChange_memo(coins, amount)
        print(f"coins={coins}, amount={amount}, result={result}, expected={expected}, {'✓ PASS' if result == expected else '✗ FAIL'}")
