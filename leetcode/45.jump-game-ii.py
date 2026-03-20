#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30204
#
# [45] 跳跃游戏 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 注意读题，是可以任意跳到 (i + j) 以内，所以直接贪心！
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=1 :
            return 0
        ans = 0
        current_end = 0  #当前步数能达到的最远位置
        farthest = 0
        for i in range(n-1):  #n-1是为什么
            farthest = max(farthest,i+nums[i])
            if i == current_end:
                ans+=1
                current_end = farthest
        return ans

    # dfs写法，简单，但是效率低，会超时
    def jump_dfs(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n-1
        def dfs(start:int,steps:int):
            nonlocal ans
            if start >= n-1:
                ans = min(ans,steps)
                return
            for i in range(1,nums[start]+1):
                dfs(start+i,steps+1)
        dfs(0,0)
        return ans
# @lc code=end



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

