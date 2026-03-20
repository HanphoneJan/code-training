#
# @lc app=leetcode.cn id=46 lang=python3
# @lcpr version=30204
#
# [46] 全排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 回溯经典题目
# 回溯定义：一种通过探索所有可能解，遇到死路就回退的算法思想。一般和DFS结合使用。
# def backtrack(路径, 选择列表):
#     if 满足结束条件:
#         收集结果
#         return
#     for 选择 in 选择列表:
#         做选择                # 将选择加入路径
#         backtrack(新路径, 新选择列表)
#         撤销选择              # 将选择从路径中移除
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        group = []
        n = len(nums)
        visited = [False] * n 

        def dfs(nums:List[int]):
            if len(group)==n:
                ans.append(group[:])
                return
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    group.append(nums[i])
                    dfs(nums)
                    group.pop()  #恢复group和visited，这就是恢复现场
                    visited[i] = False
        dfs(nums)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

