#
# @lc app=leetcode.cn id=22 lang=python3
# @lcpr version=30204
#
# [22] 括号生成
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    # 居然是回溯，又是动态规划
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = [''] * (n * 2)  # 所有括号长度都是 2n

        # 目前填了 left 个左括号，right 个右括号
        def dfs(left: int, right: int) -> None:
            if right == n:  # 填完 2n 个括号
                ans.append(''.join(path))
                return
            if left < n:  # 可以填左括号
                path[left + right] = '('  # 直接覆盖
                dfs(left + 1, right)
            if right < left:  # 可以填右括号
                path[left + right] = ')'  # 直接覆盖
                dfs(left, right + 1)

        dfs(0, 0)  # 一开始没有填括号
        return ans

# @lc code=end



#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

