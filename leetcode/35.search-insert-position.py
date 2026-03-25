#
# @lc app=leetcode.cn id=35 lang=python3
# @lcpr version=30204
#
# [35] 搜索插入位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left,right = 0,n-1
        result = 0
        while(left<=right):
            mid = int(left+(right-left)/2)
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target):
                right = mid-1
            else:
                left=mid+1
        return left
# @lc code=end



#
# @lcpr case=start
# [1,3,5,6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,5,6]\n7\n
# @lcpr case=end

#

