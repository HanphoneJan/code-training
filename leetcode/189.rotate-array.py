#
# @lc app=leetcode.cn id=189 lang=python3
# @lcpr version=30204
#
# [189] 轮转数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        # 解法一：翻转数组（原地，O(1)空间）
        self.reverse(nums, 0, n - 1)  # nums[:k] = reversed(nums[:k])，nums[:] = nums[-k:] + nums[:-k] 会创建临时列表，不是 O(1) 空间。
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], left: int, right: int) -> None:
        """辅助函数：反转数组区间 [left, right]"""
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

