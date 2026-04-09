#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30204
#
# [238] 除了自身以外数组的乘积
#


# @lcpr-template-start
from typing import List
# @lcpr-template-end
# @lc code=start
class Solution:
    """
    除了自身以外数组的乘积 - 前后缀分解

    问题描述：
    给你一个整数数组 nums，返回数组 answer，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
    题目数据保证数组 nums之中任意元素的全部前缀元素和后缀的乘积都在 32 位整数范围内。
    请不要使用除法，且在 O(n) 时间复杂度内完成此题。

    核心思路：
    对于每个位置 i，answer[i] = (nums[0] * ... * nums[i-1]) * (nums[i+1] * ... * nums[n-1])
                              = 前缀积[i] * 后缀积[i]

    优化：
    1. 先计算所有后缀积，存储在 answer 数组中
    2. 再遍历一次，用变量维护前缀积，直接乘到 answer[i] 中
    这样只需要 O(1) 额外空间（不包括输出数组）。

    时间复杂度：O(n) - 两次遍历
    空间复杂度：O(1) - 不包括输出数组，只使用一个变量
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        返回除自身以外数组的乘积
        """
        # 同时利用前后缀，第一次碰到很难想，经典题目
        # O(n) 时间复杂度，是允许多次遍历的，不要总局限在单次遍历

        n = len(nums)

        # 解法一：使用两个数组存储前后缀（O(n) 空间）
        # L[i] 表示 nums[0] 到 nums[i-1] 的乘积（i 左侧所有元素的乘积）
        # R[i] 表示 nums[i+1] 到 nums[n-1] 的乘积（i 右侧所有元素的乘积）
        # answer[i] = L[i] * R[i]

        # 解法二：O(1)空间（不算输出数组）
        # 先用 answer 数组存储后缀积
        answer = [1] * n

        # 计算后缀积：answer[i] = nums[i+1] * nums[i+2] * ... * nums[n-1]
        # 从右向左遍历
        for i in range(n - 2, -1, -1):
            answer[i] = answer[i + 1] * nums[i + 1]

        # 计算前缀积并乘到 answer 中
        # 从左向右遍历，pre 表示 nums[0] 到 nums[i-1] 的乘积
        pre = 1
        for i in range(n):
            # 此时 pre 为 nums[0] 到 nums[i-1] 的乘积，answer[i] 为后缀积
            # 直接相乘得到结果
            answer[i] *= pre
            # 更新前缀积，包含当前元素
            pre *= nums[i]

        return answer

    def productExceptSelfTwoArrays(self, nums: List[int]) -> List[int]:
        """
        使用两个数组的版本，更容易理解

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        n = len(nums)

        # L[i] 为索引 i 左侧所有元素的乘积
        L = [0] * n
        L[0] = 1  # 第一个元素左边没有元素
        for i in range(1, n):
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] 为索引 i 右侧所有元素的乘积
        R = [0] * n
        R[n - 1] = 1  # 最后一个元素右边没有元素
        for i in range(n - 2, -1, -1):
            R[i] = nums[i + 1] * R[i + 1]

        # answer[i] = L[i] * R[i]
        answer = [0] * n
        for i in range(n):
            answer[i] = L[i] * R[i]

        return answer


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    nums1 = [1, 2, 3, 4]
    result1 = sol.productExceptSelf(nums1.copy())
    print(f"Test 1: productExceptSelf([1,2,3,4]) = {result1}")
    assert result1 == [24, 12, 8, 6], f"Expected [24, 12, 8, 6], got {result1}"
    # 解释：
    # answer[0] = 2*3*4 = 24
    # answer[1] = 1*3*4 = 12
    # answer[2] = 1*2*4 = 8
    # answer[3] = 1*2*3 = 6

    # 测试用例 2：包含 0
    nums2 = [-1, 1, 0, -3, 3]
    result2 = sol.productExceptSelf(nums2.copy())
    print(f"Test 2: productExceptSelf([-1,1,0,-3,3]) = {result2}")
    assert result2 == [0, 0, 9, 0, 0], f"Expected [0, 0, 9, 0, 0], got {result2}"
    # 解释：
    # answer[0] = 1*0*(-3)*3 = 0
    # answer[1] = (-1)*0*(-3)*3 = 0
    # answer[2] = (-1)*1*(-3)*3 = 9
    # answer[3] = (-1)*1*0*3 = 0
    # answer[4] = (-1)*1*0*(-3) = 0

    # 测试用例 3：包含多个 0
    nums3 = [0, 0]
    result3 = sol.productExceptSelf(nums3.copy())
    print(f"Test 3: productExceptSelf([0,0]) = {result3}")
    assert result3 == [0, 0], f"Expected [0, 0], got {result3}"

    # 测试用例 4：单元素（边界情况，虽然题目说 n >= 2）
    nums4 = [5]
    result4 = sol.productExceptSelf(nums4.copy())
    print(f"Test 4: productExceptSelf([5]) = {result4}")
    assert result4 == [1], f"Expected [1], got {result4}"
    # 只有一个元素，左边没有元素，右边也没有元素，乘积为 1（空积）

    # 测试用例 5：负数
    nums5 = [-1, -2, -3, -4]
    result5 = sol.productExceptSelf(nums5.copy())
    print(f"Test 5: productExceptSelf([-1,-2,-3,-4]) = {result5}")
    assert result5 == [-24, -12, -8, -6], f"Expected [-24, -12, -8, -6], got {result5}"

    # 测试用例 6：两个数组版本测试
    nums6 = [1, 2, 3, 4]
    result6 = sol.productExceptSelfTwoArrays(nums6.copy())
    print(f"Test 6 (Two Arrays): productExceptSelfTwoArrays([1,2,3,4]) = {result6}")
    assert result6 == [24, 12, 8, 6], f"Expected [24, 12, 8, 6], got {result6}"

    print("\nAll tests passed!")
