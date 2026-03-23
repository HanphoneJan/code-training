#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        跳跃游戏 II - 贪心算法

        核心思想：
        题目要求到达最后位置的最少跳跃次数。由于可以跳到 i + nums[i] 范围内的任意位置，
        我们不需要尝试所有可能，而是用贪心策略：每一步都跳到能到达最远的位置。

        关键变量：
        - current_end: 当前这一步能到达的最远位置
        - farthest: 从当前范围出发，下一步能到达的最远位置
        - ans: 跳跃次数

        为什么遍历到 n-1 而不是 n？
        因为当到达最后一个位置时，不需要再跳跃了。如果遍历到 n，可能会多算一次跳跃。
        """
        n = len(nums)
        if n <= 1:
            return 0

        ans = 0           # 跳跃次数
        current_end = 0   # 当前这一步能到达的最远位置
        farthest = 0      # 下一步能到达的最远位置

        for i in range(n - 1):  # 遍历到倒数第二个位置即可
            # 更新下一步能到达的最远位置
            farthest = max(farthest, i + nums[i])

            # 到达当前步数的边界，必须跳一步
            if i == current_end:
                ans += 1
                current_end = farthest  # 更新当前步数的边界为下一步的最远位置

                # 优化：如果已经能到达终点，直接返回
                if current_end >= n - 1:
                    return ans

        return ans

    def jump_dfs(self, nums: List[int]) -> int:
        """
        DFS解法 - 暴力枚举所有可能，用于理解问题
        时间复杂度 O(k^n)，会超时，仅供学习参考
        """
        n = len(nums)
        ans = n - 1  # 初始化为最大可能值

        def dfs(start: int, steps: int) -> None:
            nonlocal ans
            if start >= n - 1:
                ans = min(ans, steps)
                return
            # 剪枝：如果当前步数已经超过最优解，停止搜索
            if steps >= ans:
                return
            # 尝试跳 1 到 nums[start] 的每一步
            for i in range(1, nums[start] + 1):
                dfs(start + i, steps + 1)

        dfs(0, 0)
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([0], 0),
        ([1, 2, 1, 1, 1], 3),
    ]

    for nums, expected in tests:
        result = sol.jump(nums)
        print(f"jump({nums}) = {result}, expected = {expected}")

