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
    """
    矩阵置零 - 原地算法

    核心思想：
    将矩阵中所有0所在的行和列都置为0。
    要求使用 O(1) 额外空间，因此需要利用矩阵本身存储信息。

    策略：
    1. 用第一行和第一列作为标记位，记录该行/列是否需要置零
    2. 先用两个变量记录第一行和第一列本身是否有零
    3. 遍历矩阵（从第二行第二列开始），如果遇到0，将对应的第一行和第一列位置置0
    4. 再次遍历，根据第一行和第一列的标记置零
    5. 最后根据之前的记录处理第一行和第一列

    时间复杂度：O(m * n)
    空间复杂度：O(1)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        # 记录第一行和第一列本身是否有零
        first_row_has_zero = 0 in matrix[0]

        # 用第一行和第一列作为标记位
        # matrix[i][0] = 0 表示第 i 行需要置零
        # matrix[0][j] = 0 表示第 j 列需要置零
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # 根据标记置零（从后往前遍历，避免影响第一列的标记）
        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 处理第一行
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0


# ========== 示例推演：matrix = [[1,1,1],[1,0,1],[1,1,1]] ==========
#
# 初始：
# [1, 1, 1]
# [1, 0, 1]
# [1, 1, 1]
#
# first_row_has_zero = False
#
# 标记阶段：发现 matrix[1][1] = 0
#   matrix[1][0] = 0, matrix[0][1] = 0
#
# 矩阵变为：
# [1, 0, 1]
# [0, 0, 1]
# [1, 1, 1]
#
# 置零阶段：
#   第1行（matrix[1][0]=0）：整行置零
#   第1列（matrix[0][1]=0）：整列置零
#
# 结果：
# [1, 0, 1]
# [0, 0, 0]
# [1, 0, 1]
# @lc code=end



#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    def print_matrix(m):
        for row in m:
            print(row)
        print()

    tests = [
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
    ]

    for matrix in tests:
        print("Before:")
        print_matrix(matrix)
        sol.setZeroes(matrix)
        print("After:")
        print_matrix(matrix)
