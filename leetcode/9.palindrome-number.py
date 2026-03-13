#
# @lc app=leetcode.cn id=9 lang=python3
# @lcpr version=30204
#
# [9] 回文数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 非常简单，爽
        if x<0 : 
            return False
        s = str(x)
        mid = len(s) // 2  
        for i in range(mid): # 头尾向中间逐个比较
            if s[i] != s[len(s)-1-i]:
                return False
        return True
# @lc code=end



#
# @lcpr case=start
# 121\n
# @lcpr case=end

# @lcpr case=start
# -121\n
# @lcpr case=end

# @lcpr case=start
# 10\n
# @lcpr case=end

#

