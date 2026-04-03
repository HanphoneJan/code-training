#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30204
#
# [198] 打家劫舍
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
# 简单但经典
# dp[i]=max(dp[i−2]+nums[i],dp[i−1])； dp[i] 表示前 i 间房屋能偷窃到的最高总金额
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 解法1：递归搜索 + 保存计算结果 = 记忆化搜索


        # 解法2：递推
        f0 = f1 =0
        for num in nums:
            f0,f1 = f1,max(f0+num,f1) 
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#

