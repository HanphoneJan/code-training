#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30204
#
# [416] 分割等和子集
#


# @lcpr-template-start
from typing import List
from functools import cache
# @lcpr-template-end

# @lc code=start
class Solution:
    """
    分割等和子集 - 0/1 背包问题

    问题描述：
    给定一个只包含正整数的非空数组，判断是否可以将这个数组分割成两个子集，
    使得两个子集的元素和相等。

    核心思路：
    这是一个经典的 0/1 背包问题。
    1. 首先计算数组总和，如果总和是奇数，直接返回 False
    2. 问题转化为：能否从数组中选出一些数，使它们的和等于总和的一半（target）
    3. 对于每个数，有选或不选两种选择

    解法一：记忆化搜索（自顶向下）
    dfs(i, target) 表示从第 i 个数开始，能否凑出和为 target

    状态转移：
    - 不选第 i 个数：dfs(i+1, target)
    - 选第 i 个数：dfs(i+1, target-nums[i])
    - 两者有一个为 True 则返回 True

    时间复杂度: O(n * target)
    空间复杂度: O(n * target)
    """
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        # 总和为奇数，无法平分
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        @cache
        def dfs(start: int, remain: int) -> bool:
            """
            从第 start 个数开始，能否凑出和为 remain
            """
            # 已经凑出目标值
            if remain == 0:
                return True
            # 剩余目标值为负 或 没有数可选了
            if remain < 0 or start >= n:
                return False

            # 选或不选当前数
            return dfs(start + 1, remain - nums[start]) or dfs(start + 1, remain)

        return dfs(0, target)


# 解法二：动态规划（自底向上，空间优化版）
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         """
#         0/1 背包 DP 解法
#
#         dp[j] 表示能否凑出和为 j
#         状态转移：dp[j] = dp[j] or dp[j - nums[i]]
#
#         时间复杂度: O(n * target)
#         空间复杂度: O(target)
#         """
#         total = sum(nums)
#         if total % 2:
#             return False
#
#         target = total // 2
#         # dp[j] 表示能否凑出和为 j
#         dp = [True] + [False] * target
#
#         for num in nums:
#             # 倒序遍历，避免重复计算
#             for j in range(target, num - 1, -1):
#                 dp[j] = dp[j] or dp[j - num]
#             # 提前退出
#             if dp[target]:
#                 return True
#
#         return dp[target]

# @lc code=end



#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：可以分割
    nums1 = [1, 5, 11, 5]
    result1 = sol.canPartition(nums1)
    print(f"Test 1: nums={nums1}")
    print(f"Result: {result1}")
    # [1,5,5] 和为 11，[11] 和为 11
    assert result1 == True, f"Expected True, got {result1}"
    print("Passed!\n")

    # 测试用例 2：无法分割
    nums2 = [1, 2, 3, 5]
    result2 = sol.canPartition(nums2)
    print(f"Test 2: nums={nums2}")
    print(f"Result: {result2}")
    # 总和为 11，无法分成两个和为 5.5 的子集
    assert result2 == False, f"Expected False, got {result2}"
    print("Passed!\n")

    # 测试用例 3：总和为奇数
    nums3 = [1, 2, 5]
    result3 = sol.canPartition(nums3)
    print(f"Test 3: nums={nums3}")
    print(f"Result: {result3}")
    assert result3 == False, f"Expected False, got {result3}"
    print("Passed!\n")

    # 测试用例 4：单个元素
    nums4 = [1]
    result4 = sol.canPartition(nums4)
    print(f"Test 4: nums={nums4}")
    print(f"Result: {result4}")
    assert result4 == False, f"Expected False, got {result4}"
    print("Passed!\n")

    # 测试用例 5：两个相同元素
    nums5 = [1, 1]
    result5 = sol.canPartition(nums5)
    print(f"Test 5: nums={nums5}")
    print(f"Result: {result5}")
    assert result5 == True, f"Expected True, got {result5}"
    print("Passed!\n")

    print("All tests passed!")
