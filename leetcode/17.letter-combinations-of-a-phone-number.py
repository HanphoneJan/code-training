#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30204
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

# 电话号码到字母的映射
MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    """
    电话号码的字母组合 - 回溯算法

    核心思想：
    每个数字对应多个字母，需要枚举所有可能的字母组合。
    使用回溯（DFS）逐位选择字母，构建所有组合。

    回溯框架：
    1. 路径：当前已构建的字母组合（path）
    2. 选择列表：当前数字对应的所有字母
    3. 终止条件：path 长度等于 digits 长度

    时间复杂度：O(3^m * 4^n)，m 是映射到3个字母的数字个数，n 是映射到4个字母的数字个数
    空间复杂度：O(m+n)，递归深度
    """
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        ans = []
        path = [''] * n  # 预分配空间，存储当前路径

        def dfs(num: int):
            """
            处理第 num 个数字
            num: 当前处理的数字索引（0-based）
            """
            if num == n:
                # 所有数字都处理完毕，得到一个完整组合
                ans.append(''.join(path))
                return

            # 遍历当前数字对应的所有字母
            for word in MAPPING[int(digits[num])]:
                path[num] = word      # 做选择
                dfs(num + 1)          # 递归处理下一个数字
                # 撤销选择（回溯）：path[num] 会被覆盖，无需显式恢复

        dfs(0)
        return ans


# ========== 示例推演：digits = "23" ==========
#
# MAPPING[2] = "abc", MAPPING[3] = "def"
#
# dfs(0): num=0, digits[0]='2', 遍历 "abc"
#   word='a': path[0]='a', dfs(1)
#     dfs(1): num=1, digits[1]='3', 遍历 "def"
#       word='d': path[1]='d', dfs(2) -> num==2, ans.append("ad")
#       word='e': path[1]='e', dfs(2) -> ans.append("ae")
#       word='f': path[1]='f', dfs(2) -> ans.append("af")
#   word='b': path[0]='b', dfs(1) -> 类似地得到 "bd", "be", "bf"
#   word='c': path[0]='c', dfs(1) -> 类似地得到 "cd", "ce", "cf"
#
# 最终结果：["ad","ae","af","bd","be","bf","cd","ce","cf"]
# @lc code=end



#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ["a", "b", "c"]),
        ("", []),
        ("79", ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz", "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]),
    ]

    for digits, expected in tests:
        result = sol.letterCombinations(digits)
        print(f"letterCombinations('{digits}') = {result}")
