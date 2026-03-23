#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        最大子数组和 - Kadane算法（动态规划思想）

        核心思想：
        遍历数组时，维护以当前位置结尾的最大子数组和。
        对于每个位置，有两种选择：
        1. 将当前元素加入前面的子数组（如果前面的和 > 0）
        2. 从当前元素开始新的子数组（如果前面的和 <= 0）

        状态转移：
        dp[i] = max(nums[i], dp[i-1] + nums[i])

        优化空间：
        只需要知道前一个状态，可以用一个变量代替数组

        为什么用 O(n) 而不是分治法 O(n log n)？
        虽然分治法也能解决，但Kadane算法更简洁高效
        """
        n = len(nums)
        # 当前子数组和（以当前元素结尾的最大子数组和）
        current_sum = nums[0]
        # 全局最大子数组和
        max_sum = nums[0]

        for i in range(1, n):
            # 关键决策：
            # 如果当前子数组和 < 0，说明前面的子数组对后面的贡献是负的
            # 不如从当前元素重新开始
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum += nums[i]

            # 更新全局最大值
            max_sum = max(max_sum, current_sum)

        return max_sum

    def maxSubArrayDP(self, nums: List[int]) -> int:
        """
        标准动态规划写法，更容易理解
        dp[i] 表示以第 i 个元素结尾的最大子数组和
        """
        n = len(nums)
        # dp[i] = 以 nums[i] 结尾的最大子数组和
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, n):
            # 状态转移：要么重新开始，要么延续前面的子数组
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            max_sum = max(max_sum, dp[i])

        return max_sum
# @lc code=end  



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8],
        [-1],
        [-2, -1],
    ]

    for nums in tests:
        result = sol.maxSubArray(nums)
        print(f"maxSubArray({nums}) = {result}")

