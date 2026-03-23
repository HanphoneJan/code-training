#
# @lc app=leetcode.cn id=74 lang=python3
# @lcpr version=30204
#
# [74] 搜索二维矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        array = []
        m,n = len(matrix),len(matrix[0])
        for i in range(m):
            array += matrix[i]
        if target in array:
            return True
        return False
    
    def searchMatrixByMid(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = -1, m * n
        while left + 1 < right:
            mid = (left + right) // 2
            x = matrix[mid // n][mid % n] #无需实际合并为一个数组的关键
            if x == target:
                return True
            if x < target:
                left = mid
            else:
                right = mid
        return False

# @lc code=end



#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#

