#
# @lc app=leetcode.cn id=6 lang=python3
# @lcpr version=30204
#
# [6] Z 字形变换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [''] * numRows # 初始化numRows个空字符串，常用，需要记住
        flag = 1  # 巧妙的用flag来控制方向
        index = 0
        for i in range(len(s)):
            rows[index] += s[i]
            if index == 0:
                flag = 1
            elif index == numRows - 1:
                flag = -1
            index += flag # 根据flag的值来决定index是加1还是减1，从而实现上下移动的效果
        return ''.join(rows)
# @lc code=end



#
# @lcpr case=start
# "PAYPALISHIRING"\n3\n
# @lcpr case=end

# @lcpr case=start
# "PAYPALISHIRING"\n4\n
# @lcpr case=end

# @lcpr case=start
# "A"\n1\n
# @lcpr case=end

#

