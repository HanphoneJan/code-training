#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 只要找出一个最大子数组即可
# 终于有道我完全靠自己做出来的了
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ans = nums[0]
        sub_array = []
        sub_sum = nums[0]
        for i in range(n):
            if nums[i] >= 0:
                if len(sub_array) ==0 or sub_sum<0:
                    sub_sum  =  nums[i]
                else:
                    sub_sum += nums[i]
                sub_array.append(nums[i])    
            elif nums[i] < 0:
                if sub_sum+nums[i]<0:
                    sub_sum = nums[i]
                    if nums[i] > sub_sum:
                        sub_array = [nums[i]]
                    else:
                        sub_array=[]
                else:
                    sub_array.append(nums[i])
                    sub_sum += nums[i]
            ans = max(sub_sum,ans)
        return ans
# @lc code=end  



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

