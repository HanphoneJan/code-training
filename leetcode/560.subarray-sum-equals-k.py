#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30204
#
# [560] 和为 K 的子数组
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 存储前缀和及其出现次数（key: 前缀和，value: 出现次数）
        prefix_count = defaultdict(int)
        prefix_count[0] = 1  # 初始状态：前缀和 0 出现 1 次（对应子数组从开头开始）
        
        current_prefix = 0  # 实时维护当前的前缀和（无需提前计算整个前缀和列表，更省内存）
        result = 0
        
        for num in nums:
            current_prefix += num  # 累加当前元素，得到截至当前的前缀和
            
            # 核心：查找需要的前缀和（current_prefix - k）的出现次数
            target = current_prefix - k
            result += prefix_count.get(target, 0)  # 没有则加 0
            
            # 将当前前缀和加入哈希表（供后续元素查询）
            prefix_count[current_prefix] += 1
        
        return result
# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#

