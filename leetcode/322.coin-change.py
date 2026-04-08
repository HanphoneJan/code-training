#
# @lc app=leetcode.cn id=322 lang=python3
# @lcpr version=30204
#
# [322] 零钱兑换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
from math import inf
from functools import cache
# 递归有额外的函数调用的开销。
# 递归中访问 memo 的顺序不是连续的，对于缓存来说不太友好，cache miss 比递推多。
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
#         def dfs(i: int, c: int) -> int:  #关键在于有返回值
#             if i < 0:
#                 return 0 if c == 0 else inf
#             if c < coins[i]:  # 只能不选
#                 return dfs(i - 1, c)
#             # 不选 vs 继续选
#             return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

#         ans = dfs(len(coins) - 1, amount)
#         return ans if ans < inf else -1

# 最优解法
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [0] + [inf] * amount
        for coin in coins:
            for cur in range(coin, amount + 1):
                f[cur] = min(f[cur], f[cur - coin] + 1)
        ans = f[amount]
        return ans if ans < inf else -1
# 我自己使用递归来做，竭尽全力依旧不是超时就是超内存
# 因为本质是回溯，没有利用到子问题，因此用cache也没用
# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         coins.sort(reverse=True)
#         res = inf
#         def dfs(start:int,count:int,amount:int):
#             nonlocal res
#             if amount<0:
#                 return
#             if count>=res:
#                 return
#             if amount == 0:
#                 res = min(res,count)
#                 return
#             for i in range(start,len(coins)):
#                 dfs(i,count+1,amount-coins[i])
#         dfs(0,0,amount)
#         if res == inf:
#             return -1 
#         return int(res)
# @lc code=end



#
# @lcpr case=start
# [1, 2, 5]\n11\n
# @lcpr case=end

# @lcpr case=start
# [2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#

