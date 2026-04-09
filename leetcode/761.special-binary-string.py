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
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) <= 2:
            return s

        # 把 s 划分成若干段合法括号字符串，记录在 substrings 中
        substrings = []
        diff = 0  # 左括号个数 - 右括号个数
        start = 0  # 子串开始下标
        for i, ch in enumerate(s):
            if ch == '1':  # 左括号
                diff += 1
            else:  # 右括号
                diff -= 1
                if diff == 0:
                    # 子串 [start, i] 是合法括号字符串，且无法继续划分
                    # 这意味着子串 [start, i] 只能是嵌套的括号，那么去掉外层的括号，递归解决 [start+1, i-1]
                    substrings.append("1" + self.makeLargestSpecial(s[start + 1: i]) + "0")
                    start = i + 1  # 下一个子串从 i+1 开始

        substrings.sort(reverse=True)
        return ''.join(substrings)


# @lc code=end



#
# @lcpr case=start
# "11011000"\n
# @lcpr case=end

# @lcpr case=start
# "10"\n
# @lcpr case=end

#

