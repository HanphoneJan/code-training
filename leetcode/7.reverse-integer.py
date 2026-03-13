#
# @lc app=leetcode.cn id=7 lang=python3
# @lcpr version=30204
#
# [7] 整数反转
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        # INT_MAX, INT_MIN = 2147483647, -2147483648
        res = 0
        while x != 0:
            digit = x % 10 if x > 0 else x % -10  # Python取模结果带符号
            # 在累加前判断是否溢出
            # 正数边界: res > 214748364 或 (res == 214748364 且 digit > 7)
            if res > 214748364 or (res == 214748364 and digit > 7):
                return 0
            # 负数边界: res < -214748364 或 (res == -214748364 且 digit < -8)
            if res < -214748364 or (res == -214748364 and digit < -8):
                return 0
            res = res * 10 + digit
            x = int(x / 10)  # 向零取整，Python的//是向下取整
        return res
# @lc code=end



#
# @lcpr case=start
# 123\n
# @lcpr case=end

# @lcpr case=start
# -123\n
# @lcpr case=end

# @lcpr case=start
# 120\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

