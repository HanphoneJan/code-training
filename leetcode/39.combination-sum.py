#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30204
#
# [39] 组合总和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 排序便于剪枝，避免重复搜索
        candidates.sort()
        ans = []
        path = []

        def dfs(start: int, target: int):
            if target == 0:
                # 保存当前路径的副本
                ans.append(path[:])
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                # 剪枝：如果当前数字已经大于剩余目标，后续更大，直接跳出
                if num > target:
                    break
                path.append(num)
                # 允许重复使用当前数字，所以下一层从 i 开始
                dfs(i, target - num)
                path.pop()  # 回溯，恢复现场

        dfs(0, target)
        return ans

            

# @lc code=end



#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#

