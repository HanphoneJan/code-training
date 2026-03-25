#
# @lc app=leetcode.cn id=70 lang=python3
# @lcpr version=30204
#
# [70] 爬楼梯
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 递归和迭代简单却经典题目
class Solution:
    def climbStairs(self, n: int) -> int:
        f1 = f0 = 1
        for i in range(2,n+1):
            new_f = f1 + f0
            f0 = f1
            f1 = new_f  
        return f1
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 3\n
# @lcpr case=end

#

