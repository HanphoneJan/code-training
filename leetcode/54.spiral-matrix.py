#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix is None or matrix[0] is None:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        visited = [ [False]*cols for _ in range(rows) ]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        total = rows * cols
        ans = [0]*total
        row, col = 0, 0
        directionIndex = 0
        for i in range(total):
            ans[i] = matrix[row][col]
            visited[row][col] = True
            nextRow, nextColumn = row + directions[directionIndex][0], col + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < cols and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            col += directions[directionIndex][1]
        return ans

# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#

