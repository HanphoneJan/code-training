#
# @lc app=leetcode.cn id=438 lang=python3
# @lcpr version=30204
#
# [438] 找到字符串中所有字母异位词
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 滑动窗口
from typing import List
from collections import Counter
# 暴力做出来
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         k = len(p)
#         n = len(s)
#         if n<k or n<0:
#             return []
#         std = Counter(p)
#         ans =[]
#         for i in range(n-k+1):
#             str = s[i:i+k]
#             if Counter(str) == std:
#                 ans.append(i)
#         return ans

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p)  # 统计 p 的每种字母的出现次数
        cnt_s = Counter()  # 统计 s 的长为 len(p) 的子串 t 的每种字母的出现次数
        ans = []

        for right, c in enumerate(s):
            cnt_s[c] += 1  # 右端点字母进入窗口

            left = right - len(p) + 1
            if left < 0:  # 窗口长度不足 len(p)
                continue

            if cnt_s == cnt_p:  # t 和 p 的每种字母的出现次数都相同
                ans.append(left)  # t 左端点下标加入答案

            cnt_s[s[left]] -= 1  # 左端点字母离开窗口

        return ans

# @lc code=end



#
# @lcpr case=start
# "cbaebabacd"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abab"\n"ab"\n
# @lcpr case=end

#

