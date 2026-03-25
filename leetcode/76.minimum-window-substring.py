#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 不定长滑动窗口问题

# 请选择 Python3 提交代码，而不是 Python
from collections import Counter

class Solution:
    """
    最小覆盖子串 - 滑动窗口

    核心思想：
    使用滑动窗口在字符串 s 中寻找包含 t 所有字符的最小子串。

    滑动窗口的关键：
    1. 右指针扩展窗口，直到窗口包含 t 的所有字符
    2. 左指针收缩窗口，在保证包含 t 所有字符的前提下，寻找最小窗口
    3. 记录最小窗口的位置

    如何判断窗口包含 t 的所有字符？
    使用 Counter 比较：cnt_s >= cnt_t 表示 s 的子串中每个字符的出现次数
    都不小于 t 中对应字符的出现次数。

    时间复杂度：O(|s| + |t|)
    空间复杂度：O(|s| + |t|)
    """
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = Counter()   # s 的子串中各字符的出现次数
        cnt_t = Counter(t)  # t 中各字符的出现次数

        ans_left, ans_right = -1, len(s)  # 记录最小窗口的左右边界
        left = 0  # 窗口左边界

        for right, c in enumerate(s):  # 右指针扩展窗口
            cnt_s[c] += 1  # 右端点字母移入窗口

            # 当窗口包含 t 的所有字符时，尝试收缩左边界
            while cnt_s >= cnt_t:
                # 更新最小窗口
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right

                # 左端点字母移出窗口
                cnt_s[s[left]] -= 1
                left += 1

        return "" if ans_left < 0 else s[ans_left: ans_right + 1]


# ========== 示例推演：s = "ADOBECODEBANC", t = "ABC" ==========
#
# 初始：left=0, cnt_t={'A':1,'B':1,'C':1}
#
# right=0, 'A': cnt_s={'A':1}，不满足包含
# right=1, 'D': cnt_s={'A':1,'D':1}
# right=2, 'O': ...
# right=3, 'B': cnt_s={'A':1,'D':1,'O':1,'B':1}
# right=4, 'E': ...
# right=5, 'C': cnt_s 包含 t，窗口 "ADOBEC"
#   更新答案，尝试收缩：
#   left=0, 移除'A'，不再包含 t，停止收缩
#
# 继续扩展...
# right=10, 'A': 再次包含 t，窗口 "BANC"
#   更新答案为更短的 "BANC"
#
# 结果："BANC"
# @lc code=end



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("aa", "aa", "aa"),
    ]

    for s, t, expected in tests:
        result = sol.minWindow(s, t)
        print(f"minWindow('{s}', '{t}') = '{result}', expected = '{expected}'")
