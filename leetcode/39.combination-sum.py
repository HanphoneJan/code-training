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
        """
        核心思想：回溯（DFS）+ 剪枝

        回溯三要素：
        - 路径（path）：当前已选择的数字组合
        - 选择列表：candidates[start:] 中可选的数字
        - 终止条件：target 减为 0（找到一个合法组合）

        去重关键：用 start 控制起始位置，每次从 i 开始（而非 i+1），
                  这样允许重复使用同一个数字，同时避免产生重复组合。

        例如 candidates=[2,3,6,7], target=7：
        选 2 → 还剩 5，继续从 2 开始选（允许重复）→ 2,2,3 ✓
        选 3 → 还剩 4，从 3 开始选 → 3 再选 3 超了，不行 → 3 选 4 不存在
        选 7 → 还剩 0，7 ✓
        """
        # 排序便于剪枝：遇到超出 target 的数字时，后续更大，可以直接 break
        candidates.sort()
        ans = []
        path = []

        def dfs(start: int, target: int):
            # 终止条件：target 恰好减为 0，当前路径是合法组合
            if target == 0:
                ans.append(path[:])  # path[:] 是浅拷贝，防止后续 path 修改影响结果
                return
            for i in range(start, len(candidates)):
                num = candidates[i]
                # 剪枝：当前数字已大于剩余目标，后续数字更大，无需继续
                if num > target:
                    break
                path.append(num)              # 做选择：将 num 加入当前路径
                dfs(i, target - num)          # 递归：允许重复使用 num，故下一层从 i 开始
                path.pop()                    # 撤销选择：回溯，恢复现场

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

