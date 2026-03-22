#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先按左端点排序（关键步骤）
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)
        if n <= 1:
            return intervals
        merged = [intervals[0]]
        for curr in intervals[1:]:
            prev = merged[-1]
            if curr[0] <= prev[1]:   # 重叠
                prev[1] = max(prev[1], curr[1])
            else:
                merged.append(curr)
        return merged
        # 写迭代和递归写法都写不出来，最后让AI完善了一下递归写法
        # def dfs(intervals: List[List[int]]) -> List[List[int]]:
        #     n = len(intervals)
        #     if n <= 1:
        #         return intervals
        #     if n == 2:
        #         a, b = intervals[0], intervals[1]
        #         # 排序后 a[0] <= b[0]，只需判断是否重叠
        #         if a[1] >= b[0]:          # 重叠
        #             return [[a[0], max(a[1], b[1])]]
        #         else:                     # 不重叠
        #             return intervals
        #     # n > 2: 处理前两个区间，再递归处理剩余部分
        #     first = intervals[0]
        #     second = intervals[1]
        #     if first[1] >= second[0]:     # 重叠，合并
        #         merged = [first[0], max(first[1], second[1])]
        #         # 递归处理合并后的区间 + 后面的区间
        #         return dfs([merged] + intervals[2:])
        #     else:                         # 不重叠，第一个区间保留
        #         return [first] + dfs(intervals[1:])

        # return dfs(intervals)

# @lc code=end



#
# @lcpr case=start
# [[1,3],[2,6],[8,10],[15,18]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,4],[4,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[4,7],[1,4]]\n
# @lcpr case=end

#

