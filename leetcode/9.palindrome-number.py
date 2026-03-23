#
# @lc app=leetcode.cn id=9 lang=python3
# @lcpr version=30204
#
# [9] 回文数
# 题目：判断一个整数是否是回文数（正读反读相同）
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        核心思想：转换为字符串后双指针比较

        回文数的特点：
        - 正读反读相同，如 121、1221
        - 负数一定不是回文数（因为有负号）
        - 末尾为0的数（除了0本身）一定不是回文数（首位不能为0）

        为什么要转字符串？
        因为整数反转可能导致溢出，而字符串处理更安全直观。
        当然也可以不转字符串，通过反转一半数字来判断。

        双指针法：
        - 一个从头开始，一个从尾开始
        - 向中间移动，逐个比较
        - 如果都相同则是回文
        """
        # 负数一定不是回文数
        # 例如：-121 反读是 121-，不等于 -121
        if x < 0:
            return False

        # 将整数转换为字符串
        s = str(x)

        # 只需要比较前半部分和后半部分
        # mid 是字符串长度的一半（向下取整）
        mid = len(s) // 2

        # 从头尾向中间逐个比较
        for i in range(mid):
            # s[i]：从左往右第 i 个字符
            # s[len(s)-1-i]：从右往左第 i 个字符
            # 例如 s="121"，i=0：s[0]='1', s[2]='1'；i=1：s[1]='2', s[1]='2'
            if s[i] != s[len(s) - 1 - i]:
                return False  # 发现不匹配的字符，不是回文

        # 所有对应位置都匹配，是回文
        return True


# ========== 示例推演：x = 121 ==========
#
# s = "121", len = 3, mid = 1
#
# i = 0：
#   s[0] = '1'
#   s[3-1-0] = s[2] = '1'
#   '1' == '1' ✓
#
# i 的范围是 range(1) = [0]，循环结束
#
# 返回 True
#
# ========== 示例：x = 10 ==========
#
# s = "10", len = 2, mid = 1
#
# i = 0：
#   s[0] = '1'
#   s[2-1-0] = s[1] = '0'
#   '1' != '0'，返回 False
# @lc code=end


# @lcpr case=start
# "121"\n
# @lcpr case=end

# @lcpr case=start
# "-121"\n
# @lcpr case=end

# @lcpr case=start
# "10"\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (11, True),
        (1221, True),
        (1231, False),
    ]

    for x, expected in tests:
        result = sol.isPalindrome(x)
        print(f"isPalindrome({x}) = {result}, expected = {expected}")
