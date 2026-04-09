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
    """
    240. 搜索二维矩阵 II

    核心思路：
    利用矩阵的排序特性：每行从左到右递增，每列从上到下递增。

    解法一：逐行二分查找
    - 对每一行进行二分查找，时间复杂度 O(m * log n)

    解法二：从右上角开始搜索（Z字形搜索）
    - 从矩阵右上角 (0, n-1) 开始
    - 如果当前值 > target，向左移动（列减1）
    - 如果当前值 < target，向下移动（行加1）
    - 如果相等，返回 True

    为什么从右上角开始？
    - 右上角的元素是一行中最大的、一列中最小的
    - 这样可以确定唯一的移动方向，不会错过目标

    时间复杂度: O(m + n) - 最多移动 m + n 步
    空间复杂度: O(1) - 只使用常数额外空间
    """

    # 解法一：逐行二分查找，时间复杂度 O(m * log n)
    def searchMatrix_binary_search(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            # 在当前行进行二分查找
            idx = bisect.bisect_left(matrix[i], target)
            if idx < len(matrix[i]) and matrix[i][idx] == target:
                return True
        return False

    # 解法二：Z字形搜索，时间复杂度 O(m + n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        # 从右上角开始
        x, y = 0, n - 1

        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                # 当前值太大，向左移动（减小）
                y -= 1
            else:
                # 当前值太小，向下移动（增大）
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


if __name__ == "__main__":
    sol = Solution()

    # 测试用例: (matrix, target, expected)
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    tests = [
        (matrix, 5, True),
        (matrix, 20, False),
        (matrix, 1, True),   # 左上角
        (matrix, 30, True),  # 右下角
        (matrix, 15, True),  # 右上角
        (matrix, 18, True),  # 左下角
        ([[1]], 1, True),
        ([[1]], 2, False),
        ([[1, 2], [3, 4]], 3, True),
    ]

    for matrix, target, expected in tests:
        result = sol.searchMatrix(matrix, target)
        print(f"target={target}, result={result}, expected={expected}, {'✓ PASS' if result == expected else '✗ FAIL'}")
