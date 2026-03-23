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
    # 回溯（DFS）生成所有有效括号组合
    def generateParenthesis(self, n: int) -> List[str]:
        """
        核心思想：回溯/DFS

        生成有效括号的约束：
        - 左括号数不能超过 n（不能放超过 n 个左括号）
        - 右括号数不能超过左括号数（没有左括号时不能放右括号）

        用 left 和 right 分别记录已放置的左括号数和右括号数：
        - 可放左括号的条件：left < n
        - 可放右括号的条件：right < left
        - 终止条件：right == n（2n 个括号全部放置完毕）

        技巧：
        - 当前填写位置 = left + right（已放字符总数）
        - 预分配 path 列表避免频繁字符串拼接
        """
        ans = []
        path = [''] * (n * 2)  # 有效括号长度固定为 2n，预分配空间

        # left：已放左括号数，right：已放右括号数
        def dfs(left: int, right: int) -> None:
            # 终止条件：已放置 n 个右括号，说明 2n 个括号全部放完
            if right == n:
                ans.append(''.join(path))
                return
            # 选择1：放左括号（前提：还有剩余左括号可用）
            if left < n:
                path[left + right] = '('  # 当前位置下标 = 已放字符总数
                dfs(left + 1, right)
            # 选择2：放右括号（前提：右括号数量比左括号少，保持合法）
            if right < left:
                path[left + right] = ')'  # 同上，当前位置下标 = left + right
                dfs(left, right + 1)

        dfs(0, 0)  # 初始：0个左括号，0个右括号
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


if __name__ == "__main__":
    sol = Solution()

    tests = [
        1,
        2,
        3,
    ]

    for n in tests:
        result = sol.generateParenthesis(n)
        print(f"generateParenthesis({n}) = {result}")
