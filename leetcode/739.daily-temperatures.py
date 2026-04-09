#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30204
#
# [739] 每日温度
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# 单调栈
# 如何判断什么时候用单调栈
# 以下两种写法都应该掌握
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i in range(n - 1, -1, -1):
            t = temperatures[i]
            while st and t >= temperatures[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1] - i
            st.append(i)
        return ans

    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     n = len(temperatures)
    #     ans = [0] * n
    #     st = []  # todolist
    #     for i, t in enumerate(temperatures):
    #         while st and t > temperatures[st[-1]]:
    #             j = st.pop()
    #             ans[j] = i - j
    #         st.append(i)
    #     return ans

# @lc code=end



#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#

