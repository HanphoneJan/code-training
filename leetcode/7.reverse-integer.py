#
# @lc app=leetcode.cn id=7 lang=python3
# @lcpr version=30204
#
# [7] 整数反转
# 题目：将32位有符号整数反转，如果反转后溢出则返回0
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        """
        核心思想：逐位反转 + 溢出检查

        整数反转方法：
        不断取最后一位数字（x % 10），然后加到结果的末尾（res * 10 + digit）

        关键点：溢出检查必须在累加之前！
        32位有符号整数范围：[-2147483648, 2147483647]
        即 [-2^31, 2^31 - 1]

        为什么用 int(x / 10) 而不是 x // 10？
        Python 的 // 是向下取整（向负无穷）
        但我们需要向零取整，所以用 int(x / 10)
        例如：-123 // 10 = -13（向下），int(-123 / 10) = -12（向零）
        """
        # 32位整数边界值
        # INT_MAX = 2147483647, INT_MIN = -2147483648
        res = 0

        while x != 0:
            # 取出 x 的最后一位数字
            # Python 取模结果带符号：-123 % 10 = 7，-123 % -10 = -3
            digit = x % 10 if x > 0 else x % -10

            # ========== 溢出检查（必须在累加前）==========
            # 正数边界检查：
            # 如果 res > 214748364，无论 digit 是多少都会溢出
            # 如果 res == 214748364，digit 必须 <= 7（因为 2147483647 的最后一位是7）
            if res > 214748364 or (res == 214748364 and digit > 7):
                return 0

            # 负数边界检查：
            # 如果 res < -214748364，无论 digit 是多少都会溢出
            # 如果 res == -214748364，digit 必须 >= -8（因为 -2147483648 的最后一位是-8）
            if res < -214748364 or (res == -214748364 and digit < -8):
                return 0

            # 累加：将 digit 放到 res 的末尾
            res = res * 10 + digit

            # 去掉 x 的最后一位
            # 注意：必须用 int(x / 10) 实现向零取整
            x = int(x / 10)

        return res


# ========== 示例推演：x = 123 ==========
#
# 初始：x = 123, res = 0
#
# 第1轮：
#   digit = 123 % 10 = 3
#   res = 0 * 10 + 3 = 3
#   x = int(123 / 10) = 12
#
# 第2轮：
#   digit = 12 % 10 = 2
#   res = 3 * 10 + 2 = 32
#   x = int(12 / 10) = 1
#
# 第3轮：
#   digit = 1 % 10 = 1
#   res = 32 * 10 + 1 = 321
#   x = int(1 / 10) = 0
#
# x == 0，循环结束，返回 321
#
# ========== 示例：x = -123 ==========
#
# 第1轮：digit = -123 % -10 = -3, res = -3, x = int(-123/10) = -12
# 第2轮：digit = -12 % -10 = -2, res = -32, x = -1
# 第3轮：digit = -1 % -10 = -1, res = -321, x = 0
# 返回 -321
# @lc code=end


# @lcpr case=start
# "123"\n
# @lcpr case=end

# @lcpr case=start
# "-123"\n
# @lcpr case=end

# @lcpr case=start
# "120"\n
# @lcpr case=end

# @lcpr case=start
# "0"\n
# @lcpr case=end

#

if __name__ == "__main__":
    import sys

    def _run_tests(cases):
        passed = 0
        for desc, func, expected in cases:
            try:
                got = func()
            except Exception as e:
                got = f"ERROR: {e}"
            ok = got == expected
            passed += ok
            print(f"  [{'PASS' if ok else 'FAIL'}] {desc}")
            if not ok:
                print(f"         Expected : {expected}")
                print(f"         Got      : {got}")
        print(f"\n  {passed}/{len(cases)} passed")
        sys.exit(0 if passed == len(cases) else 1)

    sol = Solution()
    _run_tests([
        ("123 -> 321",          lambda: sol.reverse(123),         321),
        ("-123 -> -321",        lambda: sol.reverse(-123),        -321),
        ("120 -> 21",           lambda: sol.reverse(120),         21),
        ("0 -> 0",              lambda: sol.reverse(0),           0),
        ("溢出1534236469 -> 0", lambda: sol.reverse(1534236469),  0),
        ("-2147483648 -> 0",    lambda: sol.reverse(-2147483648), 0),
    ])
