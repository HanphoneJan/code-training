#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30204
#
# [347] 前 K 个高频元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List
# 堆排序，Counter的用法
from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计频率
        freq_map = Counter(nums)
        
        # 最小堆，存储 (频率, 元素)
        heap = []
        for num, freq in freq_map.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                # 如果当前频率大于堆顶最小频率，则替换
                if freq > heap[0][0]:
                    heapq.heapreplace(heap, (freq, num))
        
        # 提取结果（顺序任意）
        return [num for _, num in heap]

# python偷懒，面试时大概率被要求重做
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         return [n[0] for n in Counter(nums).most_common(k)]

# 桶排序！！
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # 第一步：统计每个元素的出现次数
#         cnt = Counter(nums)
#         max_cnt = max(cnt.values())

#         # 第二步：把出现次数相同的元素，放到同一个桶中
#         buckets = [[] for _ in range(max_cnt + 1)]  # 也可以用 defaultdict(list)
#         for x, c in cnt.items():
#             buckets[c].append(x)

#         # 第三步：倒序遍历 buckets，把出现次数前 k 大的元素加入答案
#         ans = []
#         for bucket in reversed(buckets):
#             ans += bucket
#             # 注意题目保证答案唯一，一定会出现恰好等于 k 的情况
#             if len(ans) == k:
#                 return ans

# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,3,1,3,2]\n2\n
# @lcpr case=end

#

