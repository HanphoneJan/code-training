#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30204
#
# [198] 打家劫舍
#


# @lcpr-template-start
from typing import List
# @lcpr-template-end
# @lc code=start
class Solution:
    """
    打家劫舍 - 动态规划

    问题描述：
    你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
    影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
    如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
    给定一个代表每个房屋存放金额的非负整数数组，计算你今晚不触动警报装置的情况下，
    能够偷窃到的最高金额。

    核心思路：
    对于第 i 间房屋，有两种选择：
    1. 偷：则不能偷第 i-1 间，最大金额 = dp[i-2] + nums[i]
    2. 不偷：最大金额 = dp[i-1]

    状态转移方程：dp[i] = max(dp[i-2] + nums[i], dp[i-1])

    空间优化：
    由于 dp[i] 只依赖于前两个状态，可以用两个变量代替数组。

    时间复杂度：O(n) - 只需遍历一次数组
    空间复杂度：O(1) - 只使用两个变量
    """

    def rob(self, nums: List[int]) -> int:
        """
        返回能偷窃到的最高金额
        """
        # 解法1：递归搜索 + 保存计算结果 = 记忆化搜索

        # 解法2：递推（空间优化版）
        # f0 表示 dp[i-2]，f1 表示 dp[i-1]
        f0 = f1 = 0
        for num in nums:
            # 更新：新的 f0 = 旧的 f1，新的 f1 = max(偷当前, 不偷当前)
            f0, f1 = f1, max(f0 + num, f1)

        return f1


# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    nums1 = [1, 2, 3, 1]
    result1 = sol.rob(nums1)
    print(f"Test 1: rob([1,2,3,1]) = {result1}")
    assert result1 == 4, f"Expected 4, got {result1}"
    # 解释：偷第1间(1)和第3间(3)，总金额 = 1 + 3 = 4

    # 测试用例 2：另一个基本示例
    nums2 = [2, 7, 9, 3, 1]
    result2 = sol.rob(nums2)
    print(f"Test 2: rob([2,7,9,3,1]) = {result2}")
    assert result2 == 12, f"Expected 12, got {result2}"
    # 解释：偷第1间(2)、第3间(9)和第5间(1)，总金额 = 2 + 9 + 1 = 12

    # 测试用例 3：空数组
    nums3 = []
    result3 = sol.rob(nums3)
    print(f"Test 3: rob([]) = {result3}")
    assert result3 == 0, f"Expected 0, got {result3}"

    # 测试用例 4：单个元素
    nums4 = [5]
    result4 = sol.rob(nums4)
    print(f"Test 4: rob([5]) = {result4}")
    assert result4 == 5, f"Expected 5, got {result4}"

    # 测试用例 5：两个元素
    nums5 = [2, 1]
    result5 = sol.rob(nums5)
    print(f"Test 5: rob([2,1]) = {result5}")
    assert result5 == 2, f"Expected 2, got {result5}"
    # 解释：只能偷其中一间，选择金额较大的第1间

    # 测试用例 6：递增数组
    nums6 = [1, 2, 3, 4, 5]
    result6 = sol.rob(nums6)
    print(f"Test 6: rob([1,2,3,4,5]) = {result6}")
    assert result6 == 9, f"Expected 9, got {result6}"
    # 解释：偷第2间(2) + 第4间(4) + 第5间(5)? 不对
    # 正确：第2间(2) + 第4间(4) = 6，或者第1间(1) + 第3间(3) + 第5间(5) = 9

    print("\nAll tests passed!")
