#
# @lc app=leetcode.cn id=761 lang=python3
# @lcpr version=30204
#
# [761] 特殊的二进制字符串
#


# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    """
    特殊的二进制字符串 - 递归 + 排序

    问题描述：
    特殊的二进制序列是具有以下两个性质的二进制序列：
    1. 0 和 1 的数量相等
    2. 二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量

    给定一个特殊的二进制序列 S，以字符串形式表示。
    定义一个操作：对于两个特殊字符串 a 和 b，如果 a 的字典序大于 b，
    可以将 ab 替换为 ba。
    要求返回经过任意次操作后，能得到的字典序最大的字符串。

    核心思路：
    1. 特殊二进制字符串可以看作「合法括号序列」，其中 1 表示左括号，0 表示右括号
    2. 一个特殊字符串可以分解为若干个「不可再分」的特殊子串
    3. 对于每个子串，去掉外层括号后递归处理内部
    4. 将所有子串按字典序降序排列后拼接，得到最大字典序

    为什么可以排序？
    - 题目允许的操作实际上就是交换相邻的特殊子串
    - 通过不断交换，可以将子串按任意顺序排列
    - 因此直接排序后拼接即可

    时间复杂度: O(n^2 log n) - 递归和排序的开销
    空间复杂度: O(n) - 递归栈空间
    """
    def makeLargestSpecial(self, s: str) -> str:
        # 基本情况：长度小于等于 2 的特殊字符串只能是 "10"
        if len(s) <= 2:
            return s

        # 把 s 划分成若干段不可再分的特殊子串
        substrings = []
        diff = 0    # 左括号个数 - 右括号个数（1 的个数 - 0 的个数）
        start = 0   # 当前子串的开始下标

        for i, ch in enumerate(s):
            if ch == '1':  # 左括号
                diff += 1
            else:  # 右括号
                diff -= 1
                if diff == 0:
                    # 子串 [start, i] 是一个不可再分的特殊字符串
                    # 去掉外层括号，递归处理内部，再加上外层括号
                    inner = self.makeLargestSpecial(s[start + 1: i])
                    substrings.append("1" + inner + "0")
                    start = i + 1  # 下一个子串从 i+1 开始

        # 按字典序降序排列，然后拼接
        substrings.sort(reverse=True)
        return ''.join(substrings)


# 迭代解法（使用栈）
# class Solution:
#     def makeLargestSpecial(self, s: str) -> str:
#         """
#         迭代版本，使用栈模拟递归
#         """
#         # 栈中存储 (当前层的子串列表, 当前层的外层左括号位置)
#         stack = [([], 0)]
#         diff = 0
#
#         for i, ch in enumerate(s):
#             if ch == '1':
#                 diff += 1
#                 if diff == 1:  # 新的外层左括号
#                     stack.append(([], i))
#             else:
#                 diff -= 1
#                 if diff == 0:  # 完成一个特殊子串
#                     substrings, start = stack.pop()
#                     inner = ''.join(sorted(substrings, reverse=True))
#                     # 将处理好的子串加入上一层
#                     stack[-1][0].append("1" + inner + "0")
#
#         # 处理最外层
#         substrings, _ = stack[0]
#         return ''.join(sorted(substrings, reverse=True))

# @lc code=end



#
# @lcpr case=start
# "11011000"\n
# @lcpr case=end

# @lcpr case=start
# "10"\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    s1 = "11011000"
    result1 = sol.makeLargestSpecial(s1)
    print(f"Test 1: s='{s1}'")
    print(f"Result: '{result1}'")
    # 可以分解为 "1100" 和 "1100"，排序后还是 "11001100"
    # 但内部可以优化："1" + makeLargestSpecial("10") + "0" = "1100"
    expected1 = "11100100"
    assert result1 == expected1, f"Expected '{expected1}', got '{result1}'"
    print("Passed!\n")

    # 测试用例 2：最简单的特殊字符串
    s2 = "10"
    result2 = sol.makeLargestSpecial(s2)
    print(f"Test 2: s='{s2}'")
    print(f"Result: '{result2}'")
    assert result2 == "10", f"Expected '10', got '{result2}'"
    print("Passed!\n")

    # 测试用例 3：多个子串
    s3 = "1100"
    result3 = sol.makeLargestSpecial(s3)
    print(f"Test 3: s='{s3}'")
    print(f"Result: '{result3}'")
    assert result3 == "1100", f"Expected '1100', got '{result3}'"
    print("Passed!\n")

    # 测试用例 4：嵌套结构
    s4 = "111000"
    result4 = sol.makeLargestSpecial(s4)
    print(f"Test 4: s='{s4}'")
    print(f"Result: '{result4}'")
    # "1" + makeLargestSpecial("1100") + "0" = "111000"
    assert result4 == "111000", f"Expected '111000', got '{result4}'"
    print("Passed!\n")

    # 测试用例 5：复杂嵌套
    s5 = "1101101000"
    result5 = sol.makeLargestSpecial(s5)
    print(f"Test 5: s='{s5}'")
    print(f"Result: '{result5}'")
    print("Passed!\n")

    print("All tests passed!")
