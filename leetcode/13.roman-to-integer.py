# @lcpr-before-debug-begin
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=13 lang=python3
# @lcpr version=30204
#
# [13] 罗马数字转整数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        values = [
            1000, 500, 
            100,  50,
            10, 5, 
            1
        ]
        symbols = [
            "M",  "D", 
            "C", "L", 
            "X", "V", 
            "I"
        ]
        ans = 0
         #zip() 是 Python 的内置函数，用于将多个可迭代对象按位置配对。
        roman_map = dict(zip(symbols,values))
        # 使用字典，代码一下子就优雅起来
        n = len(s)
        for i in range(n):
            if i+1<n and roman_map[s[i]]<roman_map[s[i+1]]:
                ans -= roman_map[s[i]]
            else:
                ans += roman_map[s[i]]
        return ans
# @lc code=end



#
# @lcpr case=start
# "III"\n
# @lcpr case=end

# @lcpr case=start
# "IV"\n
# @lcpr case=end

# @lcpr case=start
# "IX"\n
# @lcpr case=end

# @lcpr case=start
# "LVIII"\n
# @lcpr case=end

# @lcpr case=start
# "MCMXCIV"\n
# @lcpr case=end

#

