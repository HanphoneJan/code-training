#
# @lc app=leetcode.cn id=283 lang=python3
# @lcpr version=30204
#
# [283] 移动零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        left = 0
        for i in range(n):
            if nums[i]==0:
                count+=1
        for i in range(n):
            if nums[i]!=0:
                nums[left]=nums[i]
                left+=1
        for i in range(n-count,n):
            nums[i]=0
# @lc code=end



#
# @lcpr case=start
# [0,1,0,3,12]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#

