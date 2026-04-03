#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30204
#
# [121] 买卖股票的最佳时机
#


# @lcpr-template-start
from typing import List

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    121. 买卖股票的最佳时机 - 贪心/动态规划

    核心思想：
    只需要买卖一次，目标是在最低点买入，最高点卖出（且卖出在买入之后）。
    遍历数组时，维护一个 "历史最低价格"，并计算 "今天卖出" 能获利的最大值。

    状态转移：
    - pre_min = min(pre_min, prices[i])  # 到第 i 天为止的最低价格
    - ans = max(ans, prices[i] - pre_min)  # 第 i 天卖出的最大利润

    为什么只需要遍历一次？
    因为对于每一天 i，最优策略一定是在 [0, i-1] 中的最低点买入。
    这个最低点可以通过一次遍历同时维护。

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        ans = 0          # 最大利润
        pre_min = prices[0]  # 历史最低价格

        for i in range(n):
            if prices[i] > pre_min:
                # 今天价格高于历史最低，可以卖出，更新最大利润
                ans = max(ans, prices[i] - pre_min)
            else:
                # 今天价格更低，更新历史最低价格
                pre_min = min(pre_min, prices[i])

        return ans


# @lc code=end


#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([7, 1, 5, 3, 6, 4], 5),    # 在 1 买入，6 卖出，利润 5
        ([7, 6, 4, 3, 1], 0),       # 价格一直跌，不交易利润为 0
        ([1, 2], 1),                # 最小例子
        ([2, 4, 1], 2),             # 先涨后跌
        ([3, 2, 6, 5, 0, 3], 4),    # 在 0 买入，3 卖出，利润 3 < 在 2 买入 6 卖出利润 4
    ]

    print("买卖股票的最佳时机 - 测试开始")
    for i, (prices, expected) in enumerate(tests, 1):
        result = sol.maxProfit(prices)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: prices={prices} -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
