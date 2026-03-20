#
# @lc app=leetcode.cn id=32 lang=python3
# @lcpr version=30204
#
# [32] 最长有效括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        核心思想：栈存储下标，计算有效括号长度

        用栈存储括号的下标（而非字符本身），以便计算有效括号区间的长度。

        规则：
        - 遇到 '('：将其下标压入栈
        - 遇到 ')'：弹出栈顶
            - 若弹出后栈为空：说明此 ')' 无法匹配，将其下标作为新的"基准"压入
            - 若弹出后栈非空：有效括号长度 = 当前下标 i - 栈顶下标

        为什么初始放 -1？
        作为"哨兵"基准，方便计算第一段有效括号的长度。
        例如 "()"：i=1 时弹出 0，栈中剩 -1，长度 = 1 - (-1) = 2。

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if not s:
            return 0
        res = 0
        # 初始化：放入哨兵 -1，作为计算有效括号长度的基准位置
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                # 左括号：记录其下标，等待右括号来匹配
                stack.append(i)
            else:
                # 右括号：弹出栈顶（与之匹配的左括号，或无效基准）
                stack.pop()
                if not stack:
                    # 栈为空：此 ')' 无法被匹配，成为新的基准
                    stack.append(i)
                else:
                    # 栈非空：以栈顶为基准，计算当前有效括号的长度
                    # i - stack[-1] 表示从基准位置到当前位置的距离
                    res = max(res, i - stack[-1])
        return res

# @lc code=end



#
# @lcpr case=start
# "(()"\n
# @lcpr case=end

# @lcpr case=start
# ")()())"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

#

