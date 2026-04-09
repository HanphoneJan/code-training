#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30204
#
# [347] 前 K 个高频元素
#


# @lcpr-template-start
from typing import List
from collections import Counter
import heapq
# @lcpr-template-end

# @lc code=start
class Solution:
    """
    前 K 个高频元素 - 堆排序解法

    问题描述：
    给定一个整数数组 nums 和一个整数 k，返回其中出现频率前 k 高的元素。
    可以按任意顺序返回答案。

    核心思路：
    1. 使用 Counter 统计每个元素的出现频率
    2. 维护一个大小为 k 的最小堆
    3. 堆顶元素是 k 个高频元素中频率最小的
    4. 当遇到频率更高的元素时，替换堆顶元素
    5. 最终堆中保留的就是频率前 k 高的元素

    为什么用最小堆而不是最大堆？
    - 最大堆需要将所有元素入堆，空间复杂度 O(n)
    - 最小堆只维护 k 个元素，空间复杂度 O(k)
    - 当 k << n 时，最小堆更省空间

    时间复杂度: O(n log k) - n 是数组长度，每次堆操作 O(log k)
    空间复杂度: O(n + k) - Counter 需要 O(n)，堆需要 O(k)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 统计每个元素的出现频率
        freq_map = Counter(nums)

        # 维护一个大小为 k 的最小堆，存储 (频率, 元素)
        # 堆顶是 k 个元素中频率最小的
        heap = []
        for num, freq in freq_map.items():
            if len(heap) < k:
                # 堆未满，直接入堆
                heapq.heappush(heap, (freq, num))
            else:
                # 堆已满，如果当前频率大于堆顶，替换堆顶
                if freq > heap[0][0]:
                    heapq.heapreplace(heap, (freq, num))

        # 提取结果，顺序任意符合题目要求
        return [num for _, num in heap]

# 其他解法参考：

# 解法二：使用 Counter.most_common()（简洁但面试时需手写堆）
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         return [n[0] for n in Counter(nums).most_common(k)]

# 解法三：桶排序（时间复杂度 O(n)）
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         # 第一步：统计每个元素的出现次数
#         cnt = Counter(nums)
#         max_cnt = max(cnt.values())
#
#         # 第二步：把出现次数相同的元素，放到同一个桶中
#         buckets = [[] for _ in range(max_cnt + 1)]
#         for x, c in cnt.items():
#             buckets[c].append(x)
#
#         # 第三步：倒序遍历 buckets，收集前 k 个高频元素
#         ans = []
#         for bucket in reversed(buckets):
#             ans += bucket
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


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    nums1, k1 = [1, 1, 1, 2, 2, 3], 2
    result1 = sol.topKFrequent(nums1, k1)
    print(f"Test 1: nums={nums1}, k={k1}")
    print(f"Result: {result1}")
    # 验证结果是否包含频率最高的两个元素（1 和 2）
    assert set(result1) == {1, 2}, f"Expected {{1, 2}}, got {set(result1)}"
    print("Passed!\n")

    # 测试用例 2：只有一个元素
    nums2, k2 = [1], 1
    result2 = sol.topKFrequent(nums2, k2)
    print(f"Test 2: nums={nums2}, k={k2}")
    print(f"Result: {result2}")
    assert result2 == [1], f"Expected [1], got {result2}"
    print("Passed!\n")

    # 测试用例 3：多个元素频率相同
    nums3, k3 = [1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2
    result3 = sol.topKFrequent(nums3, k3)
    print(f"Test 3: nums={nums3}, k={k3}")
    print(f"Result: {result3}")
    # 1 和 2 都出现了 5 次，频率最高
    assert set(result3) == {1, 2}, f"Expected {{1, 2}}, got {set(result3)}"
    print("Passed!\n")

    # 测试用例 4：k 等于数组长度
    nums4, k4 = [1, 2, 3, 4], 4
    result4 = sol.topKFrequent(nums4, k4)
    print(f"Test 4: nums={nums4}, k={k4}")
    print(f"Result: {result4}")
    assert set(result4) == {1, 2, 3, 4}, f"Expected {{1, 2, 3, 4}}, got {set(result4)}"
    print("Passed!\n")

    print("All tests passed!")
