#
# @lc app=leetcode.cn id=10 lang=python3
# @lcpr version=30204
#
# [10] 正则表达式匹配
# 题目：给定字符串 s 和模式 p，实现支持 '.' 和 '*' 的正则表达式匹配
#       '.' 匹配任意单个字符
#       '*' 匹配零个或多个前面的元素
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        核心思想：动态规划

        定义 dp[i][j]：s 的前 i 个字符能否被 p 的前 j 个字符匹配

        为什么这样定义？
        我们需要比较两个字符串的前缀，逐步扩展问题规模
        最终答案就是 dp[m][n]，即完整字符串是否匹配
        """
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            """
            辅助函数：判断 s 的第 i 个字符和 p 的第 j 个字符是否匹配

            注意：i 和 j 是计数（从1开始），所以实际索引是 i-1 和 j-1

            匹配条件：
            1. p[j-1] 是 '.' ：可以匹配任意字符
            2. p[j-1] 是普通字符：必须和 s[i-1] 完全相同
            """
            if i == 0:
                # s 的前0个字符（空串），没有任何字符可供匹配
                return False
            if p[j - 1] == '.':
                # '.' 是万能通配符，匹配任意单个字符
                return True
            # 普通字符，必须严格相等
            return s[i - 1] == p[j - 1]

        # 初始化 DP 表格
        # 大小为 (m+1) × (n+1)，因为要考虑空串的情况（前0个字符）
        # 初始值全为 False，表示默认情况下无法匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # 核心边界条件：两个空串是匹配的
        # dp[0][0] = True 表示：s 的前0个字符（空串）可以被 p 的前0个字符（空串）匹配
        dp[0][0] = True

        # 遍历所有状态
        # i 从 0 开始：s 可以是空串（需要处理 p = "a*" 匹配空串的情况）
        # j 从 1 开始：p 至少要有1个字符才有意义（p为空且s非空一定不匹配）
        for i in range(m + 1):
            for j in range(1, n + 1):

                if p[j - 1] == "*":
                    # ========== 情况1：p 的第 j 个字符是 '*' ==========
                    #
                    # '*' 的本质含义：让前面的字符（p[j-2]）出现 0 次或多次
                    # 例如 "a*" 可以表示：""（0个a）、"a"、"aa"、"aaa"...
                    #
                    # 所以我们有两种选择：

                    # 选择A：让前面的字符出现 0 次（相当于删除 "x*" 这对组合）
                    # dp[i][j-2] 表示：不用 p[j-2] 和 '*'，看前面的能否匹配
                    dp[i][j] |= dp[i][j - 2]  #按位或赋值运算符，在这里等价于or操作

                    # 选择B：让前面的字符出现 1 次或多次
                    # 前提：p[j-2] 必须能匹配 s[i-1]（当前字符）
                    if matches(i, j - 1):
                        # dp[i-1][j] 表示：s 少用一个字符，但 p 保持不变
                        # 意思是：s[i-1] 被匹配掉了，但 '*' 还可以继续匹配后面的
                        # 例如 s="aaa", p="a*"，第一个 'a' 匹配后，剩下 "aa" vs "a*" 仍需匹配
                        dp[i][j] |= dp[i - 1][j]

                else:
                    # ========== 情况2：p 的第 j 个字符是普通字符或 '.' ==========
                    #
                    # 简单匹配：当前字符必须匹配，且前面的部分也要匹配
                    # dp[i-1][j-1] 表示：s 和 p 都向前推进一位
                    if matches(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]

        # 最终答案：完整的 s 和完整的 p 能否匹配
        return dp[m][n]


# 示例推演：s = "aa", p = "a*"
#
# 初始化：dp[0][0] = True，其余为 False
#
# 处理 p[0] = 'a'（j=1）：
#   - p[0] 不是 '*'，需要 s 有字符才能匹配
#   - dp[1][1]：s[0]='a' 匹配 p[0]='a'，且 dp[0][0]=True，所以 dp[1][1]=True
#   - dp[2][1]：s[1]='a' 匹配 p[0]='a'，但 dp[1][0]=False，所以 dp[2][1]=False
#
# 处理 p[1] = '*'（j=2）：
#   - dp[0][2]：'*' 可以让 'a' 出现0次，dp[0][0]=True，所以 dp[0][2]=True
#   - dp[1][2]：
#       * 选择A（0次）：dp[1][0]=False
#       * 选择B（1次+）：p[0]='a' 匹配 s[0]='a'，dp[0][2]=True，所以 dp[1][2]=True
#   - dp[2][2]：
#       * 选择A（0次）：dp[2][0]=False
#       * 选择B（1次+）：p[0]='a' 匹配 s[1]='a'，dp[1][2]=True，所以 dp[2][2]=True
#
# 结果：dp[2][2] = True，"aa" 可以被 "a*" 匹配 ✓
# @lc code=end


# @lcpr case=start
# "aa"\n"a"\n
# 解释："a" 只能匹配一个 'a'，但 s 有两个 'a'，返回 False
# @lcpr case=end

# @lcpr case=start
# "aa"\n"a*"\n
# 解释："a*" 表示零个或多个 'a'，可以匹配 "aa"，返回 True
# @lcpr case=end

# @lcpr case=start
# "ab"\n".*"\n
# 解释：".*" 表示零个或多个任意字符，可以匹配 "ab"，返回 True
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
        ("", "a*", True),
        ("a", ".", True),
    ]

    for s, p, expected in tests:
        result = sol.isMatch(s, p)
        print(f"isMatch('{s}', '{p}') = {result}, expected = {expected}")
