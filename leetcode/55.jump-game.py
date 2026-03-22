#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30204
#
# [55] 跳跃游戏
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==1:
            return True
        max_distance = 0
        cur_distance = 0
        for i in range(n):
            cur_distance = i+nums[i]
            max_distance = max(max_distance,cur_distance)
            if i == max_distance:
                return False
            if max_distance >= n-1:
                return True
        return True
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#

