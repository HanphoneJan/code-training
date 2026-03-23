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
        """
        螺旋矩阵 - 模拟法

        核心思想：
        按照右、下、左、上的顺序遍历矩阵，遇到边界或已访问的元素时转向。

        方向定义（顺时针）：
        - 右: (0, 1)  - 列增加
        - 下: (1, 0)  - 行增加
        - 左: (0, -1) - 列减少
        - 上: (-1, 0) - 行减少

        转向条件：
        1. 超出矩阵边界
        2. 遇到已访问的元素

        优化思路（不 visited 数组）：
        可以用四个变量记录上下左右边界，到达边界后收缩边界，省掉 visited 空间
        """
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols

        # visited 数组标记已访问的位置
        visited = [[False] * cols for _ in range(rows)]

        # 四个方向：右、下、左、上（顺时针）
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction_idx = 0  # 当前方向索引

        ans = []
        row, col = 0, 0  # 当前位置

        for _ in range(total):
            # 访问当前位置
            ans.append(matrix[row][col])
            visited[row][col] = True

            # 计算下一个位置
            next_row = row + directions[direction_idx][0]
            next_col = col + directions[direction_idx][1]

            # 检查是否需要转向
            # 条件：越界 或 已访问
            if not (0 <= next_row < rows and
                    0 <= next_col < cols and
                    not visited[next_row][next_col]):
                # 顺时针转向
                direction_idx = (direction_idx + 1) % 4
                next_row = row + directions[direction_idx][0]
                next_col = col + directions[direction_idx][1]

            row, col = next_row, next_col

        return ans

    def spiralOrderOptimized(self, matrix: List[List[int]]) -> List[int]:
        """
        优化版本：不使用 visited 数组，用边界收缩
        空间复杂度 O(1)，时间复杂度 O(m*n)
        """
        if not matrix or not matrix[0]:
            return []

        rows, cols = len(matrix), len(matrix[0])
        ans = []

        # 定义四个边界
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1

        while top <= bottom and left <= right:
            # 从左到右遍历上边
            for col in range(left, right + 1):
                ans.append(matrix[top][col])
            top += 1  # 上边界下移

            # 从上到下遍历右边
            for row in range(top, bottom + 1):
                ans.append(matrix[row][right])
            right -= 1  # 右边界左移

            # 从右到左遍历下边（需要检查是否还有行）
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    ans.append(matrix[bottom][col])
                bottom -= 1  # 下边界上移

            # 从下到上遍历左边（需要检查是否还有列）
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    ans.append(matrix[row][left])
                left += 1  # 左边界右移

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

if __name__ == "__main__":
    sol = Solution()

    tests = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [[1, 2, 3]],
        [[1], [2], [3]],
    ]

    for matrix in tests:
        result = sol.spiralOrder(matrix)
        print(f"spiralOrder({matrix}) = {result}")

