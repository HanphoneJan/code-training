#
# @lc app=leetcode.cn id=12 lang=python3
# @lcpr version=30204
#
# [12] 整数转罗马数字
# 题目：将整数（1-3999）转换为罗马数字
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        """
        核心思想：贪心算法（从大到小匹配）

        罗马数字的规则：
        - 基本符号：I(1), V(5), X(10), L(50), C(100), D(500), M(1000)
        - 特殊组合：IV(4), IX(9), XL(40), XC(90), CD(400), CM(900)

        贪心策略：
        从最大的数值开始，能减就减，同时记录对应的罗马数字。
        例如 3749：
        - 3749 >= 1000，减1000，得 "M"，剩2749
        - 2749 >= 1000，减1000，得 "MM"，剩1749
        - ...

        为什么要把特殊组合也列入 values？
        例如 4 应该表示为 IV 而不是 IIII
        所以 values 中要有 4 对应的 "IV"
        """
        # 数值从大到小排列，包括特殊组合
        values = [
            1000, 900, 500, 400,   # M, CM, D, CD
            100, 90, 50, 40,       # C, XC, L, XL
            10, 9, 5, 4,           # X, IX, V, IV
            1                      # I
        ]

        # 对应的罗马数字符号
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        # 存储结果字符
        ans = []

        # 遍历每个数值
        for i in range(len(values)):
            # 计算当前数值能使用几次
            # 例如 num=3749, values[0]=1000，count = 3，表示可以用3个M
            count = num // values[i]

            # 添加 count 个当前符号
            # 例如 "M" * 3 = "MMM"
            ans.append(symbols[i] * count)

            # 减去已经处理的部分
            num -= values[i] * count

        # 拼接所有字符
        return "".join(ans)


# ========== 示例推演：num = 3749 ==========
#
# i=0, value=1000, symbol="M":
#   count = 3749 // 1000 = 3
#   ans = ["MMM"]
#   num = 3749 - 3000 = 749
#
# i=1, value=900, symbol="CM":
#   count = 749 // 900 = 0
#   ans = ["MMM", ""]
#   num 不变
#
# i=2, value=500, symbol="D":
#   count = 749 // 500 = 1
#   ans = ["MMM", "", "D"]
#   num = 749 - 500 = 249
#
# i=3, value=400, symbol="CD":
#   count = 249 // 400 = 0
#
# i=4, value=100, symbol="C":
#   count = 249 // 100 = 2
#   ans = ["MMM", "", "D", "", "CC"]
#   num = 249 - 200 = 49
#
# i=5, value=90, symbol="XC":
#   count = 49 // 90 = 0
#
# i=6, value=50, symbol="L":
#   count = 49 // 50 = 0
#
# i=7, value=40, symbol="XL":
#   count = 49 // 40 = 1
#   ans = ["MMM", "", "D", "", "CC", "", "", "XL"]
#   num = 49 - 40 = 9
#
# i=8, value=10, symbol="X": count=0
# i=9, value=9, symbol="IX": count=1, ans添加"IX", num=0
# ...
#
# 最终拼接："MMM" + "D" + "CC" + "XL" + "IX" = "MMMDCCXLIX"
# @lc code=end


# @lcpr case=start
# "3749"\n
# @lcpr case=end

# @lcpr case=start
# "58"\n
# @lcpr case=end

# @lcpr case=start
# "1994"\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        (3749, "MMMDCCXLIX"),
        (58, "LVIII"),
        (1994, "MCMXCIV"),
        (4, "IV"),
        (9, "IX"),
        (40, "XL"),
        (3999, "MMMCMXCIX"),
    ]

    for num, expected in tests:
        result = sol.intToRoman(num)
        print(f"intToRoman({num}) = '{result}', expected = '{expected}'")
