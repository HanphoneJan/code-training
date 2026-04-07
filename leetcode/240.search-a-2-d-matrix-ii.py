#
# @lc app=leetcode.cn id=240 lang=python3
# @lcpr version=30204
#
# [240] 搜索二维矩阵 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
import bisect
class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     m = len(matrix)
    #     n = len(matrix[0])
    #     for i in range(m):
    #         idx = bisect.bisect_left(matrix[i],target)
    #         if idx<len(matrix[i]) and matrix[i][idx]==target:
    #             return  True
    #     return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
# @lc code=end



#
# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n20\n
# @lcpr case=end

#

