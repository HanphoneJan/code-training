#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30204
#
# [75] 颜色分类
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针一次遍历做法
        # 不是插入元素，而是修改元素
        # p0 = p1 = 0
        # for i, x in enumerate(nums):
        #     nums[i] = 2
        #     if x <= 1:
        #         nums[p1] = 1
        #         p1 += 1
        #     if x == 0:
        #         nums[p0] = 0
        #         p0 += 1
        # 题目的本意是不让用sort(不只是库内置的sort)，我原来的做法是不恰当的
        # 计数排序，最快
        # n = len(nums)
        # n0,n1,n2 =0,0,0
        # for i in range(n):
        #     if nums[i] == 0:
        #         n0+=1
        #     elif nums[i] ==1:
        #         n1+=1
        #     else:
        #         n2+=2
        # for i in range(n):
        #     if 0<=i<n0:
        #         nums[i]=0
        #     elif n0<=i<n0+n1:
        #         nums[i]=1
        #     else:
        #         nums[i]=2
                
        # 快速排序：quick_sort(nums,0,len(nums)-1)
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

