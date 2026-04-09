#
# @lc app=leetcode.cn id=300 lang=python3
# @lcpr version=30204
#
# [300] 最长递增子序列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import bisect


class Solution:
    """
    300. 最长递增子序列 (LIS) - 动态规划 + 贪心优化

    问题定义：
    找到数组中最长的严格递增子序列的长度。
    子序列不要求连续，但要求相对顺序不变。

    解法一：动态规划 O(n^2)
    - dp[i] 表示以 nums[i] 结尾的最长递增子序列长度
    - 转移方程：dp[i] = max(dp[j] + 1) 对于所有 j < i 且 nums[j] < nums[i]
    - 初始：dp[i] = 1（每个元素自身构成长度为 1 的序列）

    解法二：贪心 + 二分查找 O(n log n)
    - 维护一个数组 tails，tails[i] 表示长度为 i+1 的递增子序列的最小末尾元素
    - 对于每个新元素，用二分查找找到它应该替换的位置
    - 如果比所有 tails 元素都大，就扩展序列长度

    贪心策略的正确性：
    - 更小的末尾元素更有利于后续扩展
    - tails 数组始终保持有序，可以用二分查找

    时间复杂度:
    - DP: O(n^2)
    - 贪心+二分: O(n log n)

    空间复杂度: O(n) - DP数组或tails数组
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        动态规划解法 O(n^2)
        dp[i] 表示以 nums[i] 结尾的最长递增子序列长度
        """
        if not nums:
            return 0

        n = len(nums)
        # dp[i] 表示以 nums[i] 结尾的最长递增子序列长度
        dp = [1] * n

        for i in range(n):
            # 检查所有在 i 之前的元素 j
            for j in range(i):
                if nums[i] > nums[j]:
                    # 如果 nums[i] 可以接在 nums[j] 后面，更新 dp[i]
                    dp[i] = max(dp[i], dp[j] + 1)

        # 返回所有 dp 值中的最大值
        return max(dp)

    def lengthOfLIS_greedy(self, nums: List[int]) -> int:
        """
        贪心 + 二分查找解法 O(n log n)
        tails[i] 表示长度为 i+1 的递增子序列的最小末尾元素
        """
        if not nums:
            return 0

        tails = []  # tails[i] = 长度为 i+1 的递增子序列的最小末尾元素

        for num in nums:
            # 在 tails 中找到第一个 >= num 的位置
            idx = bisect.bisect_left(tails, num)

            if idx == len(tails):
                # num 比所有 tails 元素都大，可以扩展序列
                tails.append(num)
            else:
                # 替换 tails[idx] 为 num，保持更小的末尾元素
                tails[idx] = num

        return len(tails)


# @lc code=end



#
# @lcpr case=start
# [10,9,2,5,3,7,101,18]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [7,7,7,7,7,7,7]\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例: (nums, expected)
    tests = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),  # [2,3,7,101]
        ([0, 1, 0, 3, 2, 3], 4),             # [0,1,2,3]
        ([7, 7, 7, 7, 7, 7, 7], 1),          # [7]
        ([1], 1),
        ([], 0),
        ([1, 2, 3, 4, 5], 5),
        ([5, 4, 3, 2, 1], 1),
    ]

    print("Testing DP solution:")
    for nums, expected in tests:
        result = sol.lengthOfLIS(nums)
        print(f"nums={nums}, result={result}, expected={expected}, {'✓ PASS' if result == expected else '✗ FAIL'}")

    print("\nTesting Greedy+Binary Search solution:")
    for nums, expected in tests:
        result = sol.lengthOfLIS_greedy(nums)
        print(f"nums={nums}, result={result}, expected={expected}, {'✓ PASS' if result == expected else '✗ FAIL'}")
