#
# @lc app=leetcode.cn id=189 lang=python3
# @lcpr version=30204
#
# [189] 轮转数组
#


# @lcpr-template-start
from typing import List
# @lcpr-template-end
# @lc code=start
class Solution:
    """
    轮转数组 - 数组翻转法

    问题描述：
    给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
    要求使用 O(1) 额外空间（原地修改）。

    核心思路：
    通过三次翻转实现数组轮转：
    1. 先翻转整个数组 [0, n-1]
    2. 再翻转前 k 个元素 [0, k-1]
    3. 最后翻转剩余元素 [k, n-1]

    为什么这样有效？
    假设原数组为 [1,2,3,4,5,6,7]，k=3，目标是 [5,6,7,1,2,3,4]
    - 整体翻转：[7,6,5,4,3,2,1]
    - 翻转前k个：[5,6,7,4,3,2,1]
    - 翻转剩余：[5,6,7,1,2,3,4] ✓

    时间复杂度：O(n) - 每个元素被访问常数次
    空间复杂度：O(1) - 原地操作，只使用几个变量
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # 处理 k > n 的情况，轮转 n 次等于原数组

        # 解法一：翻转数组（原地，O(1)空间）
        # 三次翻转实现轮转效果
        self.reverse(nums, 0, n - 1)   # 第一步：翻转整个数组
        self.reverse(nums, 0, k - 1)   # 第二步：翻转前 k 个元素
        self.reverse(nums, k, n - 1)   # 第三步：翻转剩余元素

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        """辅助函数：反转数组区间 [left, right]

        使用双指针技术，从两端向中间交换元素
        """
        # 双指针反转方法，必会
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # 解法二：复制数组（O(n)空间，非原地但符合题目要求）
    # def rotate(self, nums: List[int], k: int) -> None:
    #     n = len(nums)
    #     k %= n
    #     temp = nums[:]  # 复制原数组
    #     for i in range(n):
    #         nums[(i + k) % n] = temp[i]


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [-1,-100,3,99]\n2\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    sol.rotate(nums1, k1)
    print(f"Test 1: rotate([1,2,3,4,5,6,7], 3) = {nums1}")
    assert nums1 == [5, 6, 7, 1, 2, 3, 4], f"Expected [5, 6, 7, 1, 2, 3, 4], got {nums1}"

    # 测试用例 2：包含负数
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    sol.rotate(nums2, k2)
    print(f"Test 2: rotate([-1,-100,3,99], 2) = {nums2}")
    assert nums2 == [3, 99, -1, -100], f"Expected [3, 99, -1, -100], got {nums2}"

    # 测试用例 3：k = 0（不旋转）
    nums3 = [1, 2, 3]
    k3 = 0
    sol.rotate(nums3, k3)
    print(f"Test 3: rotate([1,2,3], 0) = {nums3}")
    assert nums3 == [1, 2, 3], f"Expected [1, 2, 3], got {nums3}"

    # 测试用例 4：k 大于数组长度
    nums4 = [1, 2]
    k4 = 5  # 相当于 k = 5 % 2 = 1
    sol.rotate(nums4, k4)
    print(f"Test 4: rotate([1,2], 5) = {nums4}")
    assert nums4 == [2, 1], f"Expected [2, 1], got {nums4}"

    # 测试用例 5：单个元素
    nums5 = [1]
    k5 = 0
    sol.rotate(nums5, k5)
    print(f"Test 5: rotate([1], 0) = {nums5}")
    assert nums5 == [1], f"Expected [1], got {nums5}"

    print("\nAll tests passed!")
