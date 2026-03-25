#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30204
#
# [48] 旋转图像
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# (i,j)→(j,n−1−i)
# i,j)→(j,n−1−i) 可以通过两次翻转操作得到：转置+行翻转
# 
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 旋转转换坐标
        # n = len(matrix)
        # top, bottom, left, right = 0, n - 1, 0, n - 1
        
        # while top < bottom and left < right:   # 实际上 top < bottom 即可，因为 left/right 同步
        #     for i in range(right - left):
        #         # 保存上边元素
        #         tmp = matrix[top][left + i]
        #         # 左边 -> 上边
        #         matrix[top][left + i] = matrix[bottom - i][left]
        #         # 下边 -> 左边
        #         matrix[bottom - i][left] = matrix[bottom][right - i]
        #         # 右边 -> 下边
        #         matrix[bottom][right - i] = matrix[top + i][right]
        #         # 上边（已保存） -> 右边
        #         matrix[top + i][right] = tmp
        #     # 收缩边界
        #     top += 1
        #     bottom -= 1
        #     left += 1
        #     right -= 1
        n = len(matrix)
        for i, row in enumerate(matrix):
            for j in range(i + 1, n):  # 遍历对角线上方元素，做转置
                row[j], matrix[j][i] = matrix[j][i], row[j]
            row.reverse()  # 行翻转

# @lc code=end



#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#

