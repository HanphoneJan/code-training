#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30204
#
# [73] 矩阵置零
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = 0 in matrix[0]  # True OR False
        # 把 matrix[i][j] 置 0 的循环，可以倒着遍历 i 行，这样可以直接修改第一列。
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            # 倒着遍历，避免提前把 matrix[i][0] 改成 0，误认为这一行要全部变成 0
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

# @lc code=end



#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#

