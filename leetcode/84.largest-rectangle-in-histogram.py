#
# @lc app=leetcode.cn id=84 lang=python3
# @lcpr version=30204
#
# [84] 柱状图中最大的矩形
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
# 单调栈经典题，和接雨水的差别是什么？为什么不能用双指针
# 对于 heights[i]，如果能快速知道左侧第一个比它矮的位置 left[i] 和右侧第一个比它矮的位置 right[i]，
# 那么以 heights[i] 为高的最大矩形宽度就是 right[i] - left[i] - 1，面积为 heights[i] * (right[i] - left[i] - 1)。
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 首尾加哨兵0，确保所有柱子都能被处理，且栈永不为空
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                # 此时栈顶是左边第一个小于h的柱子索引
                width = i - stack[-1] - 1
                max_area = max(max_area, h * width)
            stack.append(i)
        return max_area
        # 先用暴力解法做，会超时
        # n = len(heights)
        # max_area = max(heights)
        # for i in range(n):
        #     min_height = heights[i]
        #     for j in range(i + 1, n):
        #         width = j - i+1
        #         min_height = min(min_height, heights[j])
        #         max_area = max(max_area, width * min_height)
        # return max_area
# @lc code=end



#
# @lcpr case=start
# [2,1,5,6,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n
# @lcpr case=end

#

