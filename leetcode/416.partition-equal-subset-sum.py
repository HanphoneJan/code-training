#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30204
#
# [416] 分割等和子集
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 转化为选或不选问题
from typing import List
from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0:
            return False
        target = sum(nums)//2
        n = len(nums)
        @cache
        def dfs(start:int,target:int)->bool:
            if target<0 or start>=n:
                return False
            if target==0:
                return True
            # for i in range(start, n):
            #     if dfs(i+1, target - nums[i]):
            #         return True  
            # 组合递归变成背包递归
            return dfs(start+1,target-nums[start]) or dfs(start+1,target)
        return dfs(0,target)

# 递推做法
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         s = sum(nums)
#         if s % 2:
#             return False
#         s //= 2  # 注意这里把 s 减半了
#         f = [True] + [False] * s
#         s2 = 0
#         for i, x in enumerate(nums):
#             s2 = min(s2 + x, s)
#             for j in range(s2, x - 1, -1):
#                 f[j] = f[j] or f[j - x]
#             if f[s]:
#                 return True
#         return False

# @lc code=end
#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#

