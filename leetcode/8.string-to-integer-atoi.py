#
# @lc app=leetcode.cn id=8 lang=python3
# @lcpr version=30204
#
# [8] 字符串转换整数 (atoi)
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() # 和trim的区别是strip会删除unicode空格
        if not s:
            return 0
        flag = 1
        # 可以用更优雅的写法代替大量if-else
        if s[0] == '-':
            flag = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        num = 0
        for i in range(len(s)):
            if s[i] not in '0123456789':
                break
            num = num * 10 + int(s[i])
        if num * flag < -2**31:
            return -2**31
        if num * flag > 2**31 - 1:
            return 2**31 - 1
        return num * flag
# @lc code=end



#
# @lcpr case=start
# "42"\n
# @lcpr case=end

# @lcpr case=start
# " -042"\n
# @lcpr case=end

# @lcpr case=start
# "1337c0d3"\n
# @lcpr case=end

# @lcpr case=start
# "0-1"\n
# @lcpr case=end

# @lcpr case=start
# "words and 987"\n
# @lcpr case=end

#

