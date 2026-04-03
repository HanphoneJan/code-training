#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30204
#
# [131] 分割回文串
#


# @lcpr-template-start
from typing import List

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    131. 分割回文串 - 回溯算法

    核心思想：
    需要把字符串 s 分割成若干子串，使得每个子串都是回文串。
    使用回溯法枚举所有可能的分割方式。

    回溯框架：
    1. 路径：当前已分割出的回文子串列表（path）
    2. 选择列表：从当前位置 i 开始，所有可能的结束位置 j
    3. 选择条件：s[i:j+1] 必须是回文串
    4. 终止条件：i == n（已经分割到字符串末尾）

    如何判断回文？
    t == t[::-1]  # 翻转后与原字符串相同

    时间复杂度：O(n * 2^n)，每个位置可以切或不切，共 2^(n-1) 种分割方式
    空间复杂度：O(n)，递归深度
    """

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []   # 存储所有合法分割方案的列表
        path = []  # 当前路径，存储已分割出的回文子串

        def dfs(i: int):
            """
            从位置 i 开始，枚举所有可能的分割方式。
            """
            if i == n:
                # 已经分割到字符串末尾，记录当前方案
                ans.append(path.copy())
                return

            # 枚举从 i 开始到 j 结束的子串
            for j in range(i, n):
                t = s[i:j + 1]
                if t == t[::-1]:  # 是回文串才继续分割
                    path.append(t)  # 做选择：把这个回文子串加入路径
                    dfs(j + 1)      # 递归处理剩余部分
                    path.pop()      # 撤销选择：回溯

        dfs(0)
        return ans


# @lc code=end


#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("aa", [["a", "a"], ["aa"]]),
        ("abc", [["a", "b", "c"]]),
        ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
    ]

    print("分割回文串 - 测试开始")
    for i, (s, expected) in enumerate(tests, 1):
        result = sol.partition(s)
        # 排序后比较（因为结果顺序可能不同）
        result_sorted = sorted(result)
        expected_sorted = sorted(expected)
        passed = result_sorted == expected_sorted
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: s='{s}' -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
