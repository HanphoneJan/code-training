#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_dict = {}
        n = len(s)
        left,ans,result = 0,0,0
        for i in range(0,n):
            if(hash_dict.get(s[i],-1)==-1):
                ans += 1
            else:
                if left < hash_dict[s[i]]:
                    left = hash_dict[s[i]]
                ans = i - left
            hash_dict[s[i]]= i
            result = max(ans,result) 
        return result
# @lc code=end



#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

