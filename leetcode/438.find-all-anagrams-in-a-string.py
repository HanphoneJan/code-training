#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start
from typing import List
from collections import Counter
# @lcpr-template-end

# @lc code=start
class Solution:
    """
    找到字符串中所有字母异位词 - 滑动窗口

    问题描述：
    给定两个字符串 s 和 p，找到 s 中所有 p 的异位词的子串，
    返回这些子串的起始索引。不考虑答案输出的顺序。

    异位词是指由相同字母以相同数量组成的字符串，
    即字母相同但排列顺序可能不同。

    核心思路：
    使用滑动窗口 + 哈希表（Counter）来比较窗口内的字符频率。

    具体步骤：
    1. 统计 p 中每个字符的出现次数，作为标准模式
    2. 维护一个大小为 len(p) 的滑动窗口在 s 上移动
    3. 统计窗口内字符的出现次数
    4. 如果窗口内的字符频率与 p 相同，则找到一个异位词

    优化：
    - 使用 Counter 直接比较，代码简洁
    - 窗口滑动时，左边字符出窗，右边字符入窗

    时间复杂度: O(n × m) - n 是 s 的长度，m 是字符集大小（26）
    空间复杂度: O(m) - 两个 Counter 的空间
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)  # 统计 p 的每种字母的出现次数
        cnt_s = Counter()   # 统计 s 的滑动窗口内字符的出现次数
        ans = []
        k = len(p)          # 窗口大小

        for right, c in enumerate(s):
            cnt_s[c] += 1   # 右端点字母进入窗口

            left = right - k + 1
            if left < 0:    # 窗口长度不足 k
                continue

            # 比较两个 Counter 是否相等
            if cnt_s == cnt_p:
                ans.append(left)  # 找到一个异位词，记录左端点

            cnt_s[s[left]] -= 1   # 左端点字母离开窗口

        return ans


# 其他解法：数组代替 Counter（更快）
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         """
#         使用数组代替 Counter，时间复杂度 O(n)
#         """
#         m, n = len(s), len(p)
#         if m < n:
#             return []
#
#         cnt_p = [0] * 26  # p 的字符频率
#         cnt_s = [0] * 26  # 窗口的字符频率
#
#         # 初始化窗口
#         for i in range(n):
#             cnt_p[ord(p[i]) - ord('a')] += 1
#             cnt_s[ord(s[i]) - ord('a')] += 1
#
#         ans = []
#         if cnt_s == cnt_p:
#             ans.append(0)
#
#         # 滑动窗口
#         for i in range(n, m):
#             cnt_s[ord(s[i]) - ord('a')] += 1      # 右边进入
#             cnt_s[ord(s[i - n]) - ord('a')] -= 1  # 左边离开
#             if cnt_s == cnt_p:
#                 ans.append(i - n + 1)
#
#         return ans


# 暴力解法（会超时）
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         """
#         暴力解法：枚举所有子串，排序后比较
#         时间复杂度: O(n × m log m)
#         """
#         k = len(p)
#         n = len(s)
#         if n < k:
#             return []
#
#         std = sorted(p)
#         ans = []
#         for i in range(n - k + 1):
#             substr = s[i:i + k]
#             if sorted(substr) == std:
#                 ans.append(i)
#         return ans

# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    s1, p1 = "cbaebabacd", "abc"
    result1 = sol.findAnagrams(s1, p1)
    print(f"Test 1: s='{s1}', p='{p1}'")
    print(f"Result: {result1}")
    # "cba" 和 "bac" 是 "abc" 的异位词
    assert result1 == [0, 6], f"Expected [0, 6], got {result1}"
    print("Passed!\n")

    # 测试用例 2：重叠的异位词
    s2, p2 = "abab", "ab"
    result2 = sol.findAnagrams(s2, p2)
    print(f"Test 2: s='{s2}', p='{p2}'")
    print(f"Result: {result2}")
    # "ab", "ba", "ab" 都是异位词
    assert result2 == [0, 1, 2], f"Expected [0, 1, 2], got {result2}"
    print("Passed!\n")

    # 测试用例 3：s 长度小于 p
    s3, p3 = "a", "abc"
    result3 = sol.findAnagrams(s3, p3)
    print(f"Test 3: s='{s3}', p='{p3}'")
    print(f"Result: {result3}")
    assert result3 == [], f"Expected [], got {result3}"
    print("Passed!\n")

    # 测试用例 4：无匹配
    s4, p4 = "abcdef", "xyz"
    result4 = sol.findAnagrams(s4, p4)
    print(f"Test 4: s='{s4}', p='{p4}'")
    print(f"Result: {result4}")
    assert result4 == [], f"Expected [], got {result4}"
    print("Passed!\n")

    # 测试用例 5：完全匹配
    s5, p5 = "abc", "abc"
    result5 = sol.findAnagrams(s5, p5)
    print(f"Test 5: s='{s5}', p='{p5}'")
    print(f"Result: {result5}")
    assert result5 == [0], f"Expected [0], got {result5}"
    print("Passed!\n")

    print("All tests passed!")
