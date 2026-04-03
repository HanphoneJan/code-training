#
# @lc app=leetcode.cn id=118 lang=python3
# @lcpr version=30204
#
# [118] 杨辉三角
#


# @lcpr-template-start
from typing import List

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    118. 杨辉三角 - 动态规划

    核心思想：
    杨辉三角的每个数字都等于它上方两数之和。
    1. 每行的第一个和最后一个元素为 1
    2. 其他元素 = 上一行的前一列 + 上一行的当前列

    状态转移方程：
    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    时间复杂度：O(numRows²)，需要生成 numRows 行，第 i 行有 i 个元素
    空间复杂度：O(numRows²)，存储结果
    """

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        triangle = []

        for i in range(numRows):
            # 创建当前行，初始化为1（首尾元素保持为1）
            row = [1] * (i + 1)

            # 计算中间元素（首尾元素保持为1，无需计算）
            for j in range(1, i):
                # 当前元素 = 左上方的数 + 正上方的数
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle

        # 极简写法
        # c = [[1] * (i + 1) for i in range(numRows)]
        # for i in range(2, numRows):
        #     for j in range(1, i):
        #         # 左上方的数 + 正上方的数
        #         c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
        # return c


# @lc code=end


#
# @lcpr case=start
# 5\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end


if __name__ == "__main__":
    sol = Solution()

    tests = [
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (1, [[1]]),
        (2, [[1], [1, 1]]),
        (3, [[1], [1, 1], [1, 2, 1]]),
        (0, []),
    ]

    print("杨辉三角 - 测试开始")
    for i, (numRows, expected) in enumerate(tests, 1):
        result = sol.generate(numRows)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: numRows={numRows} -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
