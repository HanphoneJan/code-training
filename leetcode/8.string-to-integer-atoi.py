#
# @lc app=leetcode.cn id=8 lang=python3
# @lcpr version=30204
#
# [8] 字符串转换整数 (atoi)
# 题目：实现 C/C++ 的 atoi 函数，将字符串转换为32位有符号整数
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        """
        核心思想：按步骤解析字符串

        atoi 的处理步骤：
        1. 跳过前导空格
        2. 处理正负号
        3. 读取数字字符，直到遇到非数字或字符串结束
        4. 转换为整数并处理溢出

        注意边界情况：
        - 空字符串
        - 只有空格
        - 无数字（如 "+-12"）
        - 溢出
        """
        # 步骤1：跳过前导空格
        # strip() 删除字符串两端的空白字符（空格、制表符、换行等）
        # 和 JavaScript trim() 的区别：strip() 还会删除 unicode 空格
        s = s.strip()

        # 边界：空字符串
        if not s:
            return 0

        # 步骤2：处理符号
        sign = 1  # 默认正数

        # 检查第一个字符是否为符号
        if s[0] == '-':
            sign = -1
            s = s[1:]  # 去掉负号，处理剩余部分
        elif s[0] == '+':
            s = s[1:]  # 去掉正号，处理剩余部分

        # 步骤3：读取数字
        num = 0
        for char in s:
            # 遇到非数字字符，停止读取
            if char not in '0123456789':
                break

            # 将字符转换为数字并累加
            # num * 10：将之前的数字左移一位（乘以10）
            # int(char)：当前数字加到个位
            num = num * 10 + int(char)

        # 应用符号
        result = num * sign

        # 步骤4：处理溢出（32位有符号整数范围）
        # INT_MIN = -2^31 = -2147483648
        # INT_MAX = 2^31 - 1 = 2147483647

        if result < -2147483648:
            return -2147483648
        if result > 2147483647:
            return 2147483647

        return result


# ========== 示例推演：s = " -042" ==========
#
# 步骤1：strip() -> "-042"
#
# 步骤2：s[0] == '-'，sign = -1，s = "042"
#
# 步骤3：
#   char='0': num = 0 * 10 + 0 = 0
#   char='4': num = 0 * 10 + 4 = 4
#   char='2': num = 4 * 10 + 2 = 42
#
# 步骤4：result = 42 * (-1) = -42
#        -2147483648 <= -42 <= 2147483647，不溢出
#
# 返回：-42
#
# ========== 示例：s = "1337c0d3" ==========
#
# 步骤1：strip() -> "1337c0d3"
# 步骤2：无符号
# 步骤3：
#   '1','3','3','7' 都是数字，num = 1337
#   'c' 不是数字，停止
# 返回：1337
# @lc code=end


# @lcpr case=start
# "42"\n
# @lcpr case=end

# @lcpr case=start
# " -042"\n
# @lcpr case=end

# @lcpr case=start
# "1337c0d3"\n
# @lcpr case=end

# @lcpr case=start
# "0-1"\n
# @lcpr case=end

# @lcpr case=start
# "words and 987"\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("42", 42),
        (" -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("words and 987", 0),
        ("2147483648", 2147483647),
        ("-2147483649", -2147483648),
    ]

    for s, expected in tests:
        result = sol.myAtoi(s)
        print(f"myAtoi('{s}') = {result}, expected = {expected}")
