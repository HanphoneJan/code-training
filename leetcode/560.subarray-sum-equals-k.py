#
# @lc app=leetcode.cn id=560 lang=python3
# @lcpr version=30204
#
# [560] 和为 K 的子数组
#


# @lcpr-template-start
from typing import List
from collections import defaultdict
# @lcpr-template-end

# @lc code=start
class Solution:
    """
    和为 K 的子数组 - 前缀和 + 哈希表

    问题描述：
    给定一个整数数组和一个整数 k，找到该数组中和为 k 的连续子数组的个数。

    核心思路：
    利用前缀和的思想。定义 prefix[i] 为数组前 i 个元素的和（即到 i-1 位置的和）。
    子数组 nums[i:j] 的和 = prefix[j] - prefix[i]

    如果子数组和等于 k，则 prefix[j] - prefix[i] = k，
    即 prefix[i] = prefix[j] - k

    具体做法：
    1. 用哈希表 cnt 记录各个前缀和出现的次数
    2. 初始化 cnt[0] = 1，表示前缀和为 0 的路径有 1 条
    3. 遍历数组，累加得到当前前缀和 curr_sum
    4. 以当前位置结尾的和为 k 的子数组个数 = cnt[curr_sum - k]
    5. 将当前前缀和加入哈希表

    为什么不能用滑动窗口？
    因为数组中包含负数，当右指针右移时，无法确定左指针应该左移还是右移。

    时间复杂度: O(n) - 只遍历一次数组
    空间复杂度: O(n) - 哈希表空间
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)  # 记录前缀和出现的次数
        cnt[0] = 1              # 前缀和为 0 的子数组有 1 个（空数组）
        ans = 0                 # 和为 k 的子数组个数
        curr_sum = 0            # 当前前缀和

        for x in nums:
            # 更新当前前缀和
            curr_sum += x
            # 以当前位置结尾的和为 k 的子数组个数
            # 即之前有多少个前缀和等于 curr_sum - k
            ans += cnt[curr_sum - k]
            # 记录当前前缀和的出现次数
            cnt[curr_sum] += 1

        return ans


# 另一种写法（更常见的顺序）
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         cnt = defaultdict(int)
#         cnt[0] = 1
#         ans = s = 0
#         for x in nums:
#             s += x
#             ans += cnt[s - k]
#             cnt[s] += 1
#         return ans

# 暴力解法（会超时）
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         """
#         枚举所有子数组，计算和
#         时间复杂度: O(n^2)
#         """
#         n = len(nums)
#         ans = 0
#         for i in range(n):
#             s = 0
#             for j in range(i, n):
#                 s += nums[j]
#                 if s == k:
#                     ans += 1
#         return ans

# @lc code=end



#
# @lcpr case=start
# [1,1,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    nums1, k1 = [1, 1, 1], 2
    result1 = sol.subarraySum(nums1, k1)
    print(f"Test 1: nums={nums1}, k={k1}")
    print(f"Result: {result1}")
    # [1,1] 和 [1,1]（两个 1+1）
    assert result1 == 2, f"Expected 2, got {result1}"
    print("Passed!\n")

    # 测试用例 2：
    nums2, k2 = [1, 2, 3], 3
    result2 = sol.subarraySum(nums2, k2)
    print(f"Test 2: nums={nums2}, k={k2}")
    print(f"Result: {result2}")
    # [1,2] 和 [3]
    assert result2 == 2, f"Expected 2, got {result2}"
    print("Passed!\n")

    # 测试用例 3：包含负数
    nums3, k3 = [1, -1, 0], 0
    result3 = sol.subarraySum(nums3, k3)
    print(f"Test 3: nums={nums3}, k={k3}")
    print(f"Result: {result3}")
    # [1,-1], [0], [1,-1,0]
    assert result3 == 3, f"Expected 3, got {result3}"
    print("Passed!\n")

    # 测试用例 4：单个元素
    nums4, k4 = [1], 1
    result4 = sol.subarraySum(nums4, k4)
    print(f"Test 4: nums={nums4}, k={k4}")
    print(f"Result: {result4}")
    assert result4 == 1, f"Expected 1, got {result4}"
    print("Passed!\n")

    # 测试用例 5：没有匹配
    nums5, k5 = [1, 2, 3], 10
    result5 = sol.subarraySum(nums5, k5)
    print(f"Test 5: nums={nums5}, k={k5}")
    print(f"Result: {result5}")
    assert result5 == 0, f"Expected 0, got {result5}"
    print("Passed!\n")

    # 测试用例 6：多个相同前缀和
    nums6, k6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0
    result6 = sol.subarraySum(nums6, k6)
    print(f"Test 6: nums=[0]*10, k={k6}")
    print(f"Result: {result6}")
    # C(10,2) + 10 = 55 个子数组和为 0
    assert result6 == 55, f"Expected 55, got {result6}"
    print("Passed!\n")

    print("All tests passed!")
