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
                """
        合并区间 - 贪心算法

        核心思想：
        1. 按区间左端点排序（关键步骤）
        2. 遍历排序后的区间，维护一个"当前合并区间"
        3. 如果当前区间与合并区间重叠，扩展合并区间
        4. 如果不重叠，保存合并区间，开始新区间

        为什么排序？
        排序后，只需要比较当前区间的左端点与合并区间的右端点，
        就能判断是否重叠，时间复杂度 O(n log n)

        重叠判断：
        curr[0] <= prev[1] 表示重叠（当前区间的左端点在上一个区间内）
        """
        # 按左端点排序（关键步骤）
        intervals.sort(key=lambda x: x[0])
        n = len(intervals)

        if n <= 1:
            return intervals

        merged = [intervals[0]]  # 初始化 merged 为第一个区间

        for curr in intervals[1:]:
            prev = merged[-1]  # 上一个合并后的区间

            # 检查是否重叠：当前区间的左端点 <= 上一个区间的右端点
            if curr[0] <= prev[1]:
                # 重叠，合并区间：更新右端点为两者的最大值
                prev[1] = max(prev[1], curr[1])
            else:
                # 不重叠，添加新区间
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

if __name__ == "__main__":
    sol = Solution()

    tests = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[4, 7], [1, 4]],
        [[1, 2]],
    ]

    for intervals in tests:
        result = sol.merge(intervals)
        print(f"merge({intervals}) = {result}")

