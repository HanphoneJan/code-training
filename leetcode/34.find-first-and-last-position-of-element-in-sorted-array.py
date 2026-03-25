#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30204
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left , right = 0 , n-1
        result_left,result_right = -1, -1
        while (left <= right) :  #当搜索区间有效时继续
            mid = int(left + (right - left) / 2)  # 防止溢出的中间值计算
            if (nums[mid] == target) :
                result_left = mid
                right = mid -1
            elif (nums[mid] < target):
                left = mid + 1;  # 目标在右半区
            else:
                right = mid - 1;  # 目标在左半区
        left,right = 0 ,n-1
        while(left<=right):
            mid = int(left+(right-left)/2)
            if(nums[mid]==target):
                result_right = mid
                left = mid+1
            elif(nums[mid]>target):
                right = mid -1
            else:
                left = mid+1
        return [result_left,result_right];   #未找到目标  
# @lc code=end



#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#

