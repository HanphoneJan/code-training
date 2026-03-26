#
# @lc app=leetcode.cn id=131 lang=python3
# @lcpr version=30204
#
# [131] 分割回文串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 知道是回溯，但是不会写，嘻嘻
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []
        def dfs(i:int):
            if i==n:
                ans.append(path.copy())
                return
            for j in range(i,n):
                t = s[i:j+1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return ans
# @lc code=end



#
# @lcpr case=start
# "aab"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n
# @lcpr case=end

#

