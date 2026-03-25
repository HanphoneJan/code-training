#
# @lc app=leetcode.cn id=17 lang=python3
# @lcpr version=30204
#
# [17] 电话号码的字母组合
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
MAPPING = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n==0:return []
        ans = []
        path = ['']*n
        def dfs(num:int):
            if num == n:
                ans.append(''.join(path))
                return
            for word in MAPPING[int(digits[num])]:
                path[num] = word
                dfs(num+1)
        dfs(0)
        return ans

             
# @lc code=end



#
# @lcpr case=start
# "23"\n
# @lcpr case=end

# @lcpr case=start
# "2"\n
# @lcpr case=end

#

