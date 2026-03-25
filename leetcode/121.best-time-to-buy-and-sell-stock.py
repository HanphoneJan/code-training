#
# @lc app=leetcode.cn id=121 lang=python3
# @lcpr version=30204
#
# [121] 买卖股票的最佳时机
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 难得有这么简单的题，感动哭了
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        ans = 0
        pre_min = prices[0]
        for i in range(n):
            if prices[i]>pre_min:
                ans = max(ans,prices[i]-pre_min)
            else:
                pre_min = min(pre_min,prices[i])
        return ans
# @lc code=end




#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

