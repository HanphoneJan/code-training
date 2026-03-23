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
        def quick_sort(arr, left, right):
            if left >= right:
                return
            
            pivot = partition(arr, left, right)
            quick_sort(arr, left, pivot - 1)
            quick_sort(arr, pivot + 1, right)

        def partition(arr, left, right):
            pivot = arr[right]
            i = left - 1
            
            for j in range(left, right):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[right] = arr[right], arr[i + 1]
            return i + 1
        quick_sort(nums,0,len(nums)-1)
# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

