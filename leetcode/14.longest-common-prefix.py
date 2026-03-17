#
# @lc app=leetcode.cn id=14 lang=python3
# @lcpr version=30204
#
# [14] 最长公共前缀
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = ""
        i = 0
        # 完全没有必要用while，外层直接用strs[0]会更清晰，我是大傻瓜
        while True:
            if i<len(strs[0]):
                word = strs[0][i]
            for str in strs:
                if i>=len(str) or str[i] != word:
                    return ans
            ans += strs[0][i] 
            i += 1

            

# @lc code=end



#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
# @lcpr case=end

#

