#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30204
#
# [238] 除了自身以外数组的乘积
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 同时利用前后缀，第一次碰到很难想，经典题目
#  O(n) 时间复杂度，是允许多次遍历的，不要总局限在单次遍历
from typing import List
class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     answer = [None] * n
    #     length = len(nums)
        
    #     # L 和 R 分别表示左右两侧的乘积列表
    #     L, R, answer = [0]*length, [0]*length, [0]*length
        
    #     # L[i] 为索引 i 左侧所有元素的乘积
    #     # 对于索引为 '0' 的元素，因为左侧没有元素，所以 L[0] = 1
    #     L[0] = 1
    #     for i in range(1, length):
    #         L[i] = nums[i - 1] * L[i - 1]
        
    #     # R[i] 为索引 i 右侧所有元素的乘积
    #     # 对于索引为 'length-1' 的元素，因为右侧没有元素，所以 R[length-1] = 1
    #     R[length - 1] = 1
    #     for i in reversed(range(length - 1)):
    #         R[i] = nums[i + 1] * R[i + 1]

    #     # 对于索引 i，除 nums[i] 之外其余各元素的乘积就是左侧所有元素的乘积乘以右侧所有元素的乘积
    #     for i in range(length):
    #         answer[i] = L[i] * R[i]
        
    #     return answer

    # O(1)空间（不算输出数组）
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        pre = 1
        for i, x in enumerate(nums):
            # 此时 pre 为 nums[0] 到 nums[i-1] 的乘积，直接乘到 suf[i] 中
            suf[i] *= pre
            pre *= x

        return suf


# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

