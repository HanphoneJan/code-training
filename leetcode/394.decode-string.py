#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#


# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    """
    字符串解码 - 栈解法

    问题描述：
    给定一个经过编码的字符串，返回它解码后的字符串。
    编码规则是：k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。
    注意 k 保证为正整数。

    核心思路：
    使用栈来处理嵌套结构。遇到 '[' 时将当前状态（已解码字符串和重复次数）入栈，
    遇到 ']' 时出栈并解码。

    具体步骤：
    1. 遍历字符串，遇到数字则解析完整数字
    2. 遇到 '[' 将当前字符串和数字入栈，重置状态
    3. 遇到 ']' 出栈，将括号内的字符串重复指定次数
    4. 遇到字母直接加入当前字符串

    时间复杂度: O(n * k) - n 是字符串长度，k 是最大重复次数
    空间复杂度: O(n) - 栈的深度
    """
    def decodeString(self, s: str) -> str:
        ptr = 0
        stack = []
        n = len(s)

        def get_digits() -> str:
            """解析连续的数字字符"""
            nonlocal ptr
            start = ptr
            while ptr < n and s[ptr].isdigit():
                ptr += 1
            return s[start:ptr]

        while ptr < n:
            cur = s[ptr]
            if cur.isdigit():
                # 获取完整数字并入栈
                digits = get_digits()
                stack.append(digits)
            elif cur.isalpha() or cur == '[':
                # 字母或 '[' 直接入栈
                stack.append(cur)
                ptr += 1
            else:  # cur == ']'
                ptr += 1   # 跳过 ']'
                # 收集括号内的子串（逆序弹出）
                sub = []
                while stack and stack[-1] != '[':
                    sub.append(stack.pop())
                sub.reverse()
                # 弹出 '['
                stack.pop()
                # 弹出数字并转为整数
                rep_time = int(stack.pop())
                # 构造重复字符串
                decoded_part = ''.join(sub) * rep_time
                stack.append(decoded_part)

        return ''.join(stack)

# 其他解法：递归解法
# class Solution:
#     def decodeString(self, s: str) -> str:
#         """
#         递归解法：遇到 '[' 递归解码，遇到 ']' 返回
#         """
#         def dfs(i):
#             res = ''
#             num = 0
#             while i < len(s):
#                 if s[i].isdigit():
#                     num = num * 10 + int(s[i])
#                 elif s[i] == '[':
#                     # 递归解码括号内的内容
#                     sub, i = dfs(i + 1)
#                     res += sub * num
#                     num = 0
#                 elif s[i] == ']':
#                     return res, i
#                 else:
#                     res += s[i]
#                 i += 1
#             return res, i
#
#         return dfs(0)[0]

# @lc code=end



#
# @lcpr case=start
# "3[a]2[bc]"\n
# @lcpr case=end

# @lcpr case=start
# "3[a2[c]]"\n
# @lcpr case=end

# @lcpr case=start
# "2[abc]3[cd]ef"\n
# @lcpr case=end

# @lcpr case=start
# "abc3[cd]xyz"\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    s1 = "3[a]2[bc]"
    result1 = sol.decodeString(s1)
    print(f"Test 1: s='{s1}'")
    print(f"Result: '{result1}'")
    assert result1 == "aaabcbc", f"Expected 'aaabcbc', got '{result1}'"
    print("Passed!\n")

    # 测试用例 2：嵌套括号
    s2 = "3[a2[c]]"
    result2 = sol.decodeString(s2)
    print(f"Test 2: s='{s2}'")
    print(f"Result: '{result2}'")
    assert result2 == "accaccacc", f"Expected 'accaccacc', got '{result2}'"
    print("Passed!\n")

    # 测试用例 3：多个括号和平铺字符
    s3 = "2[abc]3[cd]ef"
    result3 = sol.decodeString(s3)
    print(f"Test 3: s='{s3}'")
    print(f"Result: '{result3}'")
    assert result3 == "abcabccdcdcdef", f"Expected 'abcabccdcdcdef', got '{result3}'"
    print("Passed!\n")

    # 测试用例 4：括号在中间
    s4 = "abc3[cd]xyz"
    result4 = sol.decodeString(s4)
    print(f"Test 4: s='{s4}'")
    print(f"Result: '{result4}'")
    assert result4 == "abccdcdcdxyz", f"Expected 'abccdcdcdxyz', got '{result4}'"
    print("Passed!\n")

    # 测试用例 5：多位数重复
    s5 = "100[leetcode]"
    result5 = sol.decodeString(s5)
    print(f"Test 5: s='{s5}'")
    print(f"Result length: {len(result5)}")
    assert result5 == "leetcode" * 100, f"Expected 'leetcode' repeated 100 times"
    print("Passed!\n")

    print("All tests passed!")
