#
# @lc app=leetcode.cn id=295 lang=python3
# @lcpr version=30204
#
# [295] 数据流的中位数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 数据结构题，排序题
# 先实现，再考虑如何优化
# 如果聚焦于有序的思路，那就用二叉搜索树等等结构维护
# 但是题目关键在于只需做到快速找中位数，那么就从
# class MedianFinder:
#     def __init__(self):
#         self.left = []  # 最大堆
#         self.right = []  # 最小堆

#     def addNum(self, num: int) -> None:
#         # heappush_max 和 heappushpop_max 是python3.14的API
#         if len(self.left) == len(self.right):
#             heappush_max(self.left, heappushpop(self.right, num))
#         else:
#             heappush(self.right, heappushpop_max(self.left, num))

#     def findMedian(self) -> float:
#         if len(self.left) > len(self.right):
#             return self.left[0]
#         return (self.left[0] + self.right[0]) / 2
    
from heapq import heappush,heappushpop

class MedianFinder:
    def __init__(self):
        self.A = [] # 小顶堆，保存较大的一半
        self.B = [] # 大顶堆，保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.B, -heappushpop(self.A, num))
        else:
            heappush(self.A, -heappushpop(self.B, -num))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0


        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end



