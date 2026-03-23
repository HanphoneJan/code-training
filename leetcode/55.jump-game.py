#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30204
#
# [55] 跳跃游戏
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        跳跃游戏 - 贪心算法

        核心思想：
        不需要真的模拟每一步跳跃，只需要记录能到达的最远位置。
        如果当前位置超过了能到达的最远位置，说明无法继续前进。

        关键变量：
        - max_reach: 从起点出发，能到达的最远位置

        遍历策略：
        1. 对于每个位置 i，检查 i 是否在可达范围内 (i <= max_reach)
        2. 更新 max_reach = max(max_reach, i + nums[i])
        3. 如果 max_reach >= n-1，说明可以到达终点
        4. 如果 i > max_reach，说明当前位置不可达，返回 False

        为什么用贪心而不是DP？
        因为只需要知道"能否到达"，不需要知道"最少几步"或"多少种方法"，
        贪心可以在线性时间内解决。
        """
        n = len(nums)
        if n <= 1:
            return True

        max_reach = 0  # 能到达的最远位置

        for i in range(n):
            # 如果当前位置超过了最远可达位置，无法继续前进
            if i > max_reach:
                return False

            # 更新最远可达位置
            max_reach = max(max_reach, i + nums[i])

            # 提前退出：已经可以到达终点
            if max_reach >= n - 1:
                return True

        return True
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [0],
        [2, 0, 0],
        [1, 0, 1, 0],
    ]

    for nums in tests:
        result = sol.canJump(nums)
        print(f"canJump({nums}) = {result}")

