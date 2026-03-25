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
    """
    搜索二维矩阵 - 二分查找

    核心思想：
    矩阵每行从左到右递增，每行第一个数大于上一行最后一个数。
    可以将二维矩阵视为一个有序的一维数组进行二分查找。

    虚拟索引转换：
    对于虚拟索引 idx，对应的矩阵位置为：
    - 行号：idx // n
    - 列号：idx % n

    时间复杂度：O(log(m*n)) = O(log m + log n)
    空间复杂度：O(1)
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """解法一：展平后查找（简单但额外空间 O(m*n)）"""
        array = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            array += matrix[i]
        return target in array

    def searchMatrixByMid(self, matrix: List[List[int]], target: int) -> bool:
        """解法二：虚拟索引二分查找（最优，O(1)空间）"""
        m, n = len(matrix), len(matrix[0])
        left, right = -1, m * n

        while left + 1 < right:
            mid = (left + right) // 2
            # 将一维索引转换为二维坐标
            x = matrix[mid // n][mid % n]
            if x == target:
                return True
            if x < target:
                left = mid
            else:
                right = mid
        return False


# ========== 示例推演：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 ==========
#
# m=3, n=4, 虚拟数组长度 12
# left=-1, right=12
#
# mid=5, matrix[5//4][5%4] = matrix[1][1] = 11 > 3, right=5
# mid=2, matrix[2//4][2%4] = matrix[0][2] = 5 > 3, right=2
# mid=0, matrix[0][0] = 1 < 3, left=0
# mid=1, matrix[0][1] = 3 == 3, 返回 True
# @lc code=end



#
# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3\n
# @lcpr case=end

# @lcpr case=start
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n13\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1]], 1, True),
        ([[1]], 2, False),
    ]

    for matrix, target, expected in tests:
        result = sol.searchMatrixByMid(matrix, target)
        print(f"searchMatrix({matrix}, {target}) = {result}, expected = {expected}")
