#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30204
#
# [5] 最长回文子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        start, end = 0, 0
        for i in range(len(s)):
            # 奇数长度回文串
            l1, r1 = expandAroundCenter(i, i)
            # 偶数长度回文串
            l2, r2 = expandAroundCenter(i, i + 1)
            
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        
        return s[start:end + 1]
# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

