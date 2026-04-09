#
# @lc app=leetcode.cn id=957 lang=python3
# @lcpr version=30204
#
# [957] N 天后的牢房
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
class Solution(object):
    def prisonAfterNDays(self, cells, N):
        def nextday(cells):
            return [int(i > 0 and i < 7 and cells[i-1] == cells[i+1])
                    for i in xrange(8)]

        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = nextday(cells)

        return cells

# @lc code=end



#
# @lcpr case=start
# [0,1,0,1,1,0,0,1]\n7\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,1,0,0,1,0]\n1000000000\n
# @lcpr case=end

#

