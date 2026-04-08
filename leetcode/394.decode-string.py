#
# @lc app=leetcode.cn id=394 lang=python3
# @lcpr version=30204
#
# [394] 字符串解码
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 栈或者递归
class Solution:
    def decodeString(self, s: str) -> str:
        ptr = 0
        stack = []
        n = len(s)

        def get_digits() -> str:
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
                # 收集括号内的子串（逆序）
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

