# @lcpr-before-debug-begin
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=13 lang=python3
# @lcpr version=30204
#
# [13] 罗马数字转整数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        核心思想：遍历字符串，判断加减法

        罗马数字规则：
        - 大多数情况下从左到右累加，如 III = 3，VIII = 8
        - 特殊减法规则：若当前符号比右边的符号小，则减去当前值
          例如：IV = 5-1 = 4，IX = 10-1 = 9，XL = 50-10 = 40

        时间复杂度：O(n)，遍历字符串一次
        空间复杂度：O(1)，字典大小固定为 7
        """
        # 基本罗马数字符号及其对应值
        values = [
            1000, 500,
            100,  50,
            10, 5,
            1
        ]
        symbols = [
            "M",  "D",
            "C", "L",
            "X", "V",
            "I"
        ]
        ans = 0
        # zip() 将两个列表按位置配对，dict() 将其转为字典
        # 结果：{"M": 1000, "D": 500, "C": 100, ...}
        roman_map = dict(zip(symbols, values))

        n = len(s)
        for i in range(n):
            # 减法规则：当前符号比右边的符号小时，减去当前值
            # 例如 IX：I(1) < X(10)，所以 ans -= 1，然后 ans += 10，合计 = 9
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
                ans -= roman_map[s[i]]
            else:
                # 正常情况：直接累加当前符号的值
                ans += roman_map[s[i]]
        return ans
# @lc code=end



#
# @lcpr case=start
# "III"\n
# @lcpr case=end

# @lcpr case=start
# "IV"\n
# @lcpr case=end

# @lcpr case=start
# "IX"\n
# @lcpr case=end

# @lcpr case=start
# "LVIII"\n
# @lcpr case=end

# @lcpr case=start
# "MCMXCIV"\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("MMMCMXCIX", 3999),
    ]

    for s, expected in tests:
        result = sol.romanToInt(s)
        print(f"romanToInt('{s}') = {result}, expected = {expected}")
