#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30204
#
# [215] 数组中的第K个最大元素
#


# @lcpr-template-start
from typing import List
from random import randint
# @lcpr-template-end
# @lc code=start
class Solution:
    """
    数组中的第K个最大元素 - 快速选择算法

    问题描述：
    给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
    请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

    核心思路：
    快速选择算法是快速排序的变种，利用 partition 操作在平均 O(n) 时间内找到第 k 大元素。

    算法步骤：
    1. 随机选择一个基准元素 pivot
    2. 将数组划分为三部分：< pivot, = pivot, > pivot
    3. 根据 k 的位置决定递归哪一部分

    为什么平均是 O(n)？
    每次 partition 后，只需要处理一半的数据：
    T(n) = n + n/2 + n/4 + ... = 2n = O(n)

    时间复杂度：
    - 平均：O(n)
    - 最坏：O(n²) - 当每次 pivot 都选到最值时

    空间复杂度：O(1) - 原地操作（递归栈空间 O(log n)）
    """

    def partition(self, nums: List[int], left: int, right: int) -> int:
        """
        在子数组 [left, right] 中随机选择一个基准元素 pivot
        根据 pivot 重新排列子数组 [left, right]
        重新排列后，<= pivot 的元素都在 pivot 的左侧，>= pivot 的元素都在 pivot 的右侧
        返回 pivot 在重新排列后的 nums 中的下标

        特别地，如果子数组的所有元素都等于 pivot，我们会返回子数组的中心下标，避免退化
        """

        # 1. 在子数组 [left, right] 中随机选择一个基准元素 pivot
        i = randint(left, right)
        pivot = nums[i]
        # 把 pivot 与子数组第一个元素交换，避免 pivot 干扰后续划分，从而简化实现逻辑
        nums[i], nums[left] = nums[left], nums[i]

        # 2. 相向双指针遍历子数组 [left + 1, right]
        # 循环不变量：在循环过程中，子数组的数据分布始终如下图
        # [ pivot | <=pivot | 尚未遍历 | >=pivot ]
        #   ^                 ^     ^         ^
        #   left              i     j         right

        i, j = left + 1, right
        while True:
            while i <= j and nums[i] < pivot:
                i += 1
            # 此时 nums[i] >= pivot

            while i <= j and nums[j] > pivot:
                j -= 1
            # 此时 nums[j] <= pivot

            if i >= j:
                break

            # 维持循环不变量
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        # 循环结束后
        # [ pivot | <=pivot | >=pivot ]
        #   ^             ^   ^     ^
        #   left          j   i     right

        # 3. 把 pivot 与 nums[j] 交换，完成划分（partition）
        # 为什么与 j 交换？
        # 如果与 i 交换，可能会出现 i = right + 1 的情况，已经下标越界了，无法交换
        # 另一个原因是如果 nums[i] > pivot，交换会导致一个大于 pivot 的数出现在子数组最左边，不是有效划分
        # 与 j 交换，即使 j = left，交换也不会出错
        nums[left], nums[j] = nums[j], nums[left]

        # 交换后
        # [ <=pivot | pivot | >=pivot ]
        #               ^
        #               j

        # 返回 pivot 的下标
        return j

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        返回数组中第 k 个最大的元素

        参数：
            nums: 整数数组
            k: 第 k 大（1 <= k <= len(nums)）
        """
        n = len(nums)
        # 第 k 大元素在升序数组中的下标是 n - k
        # 例如：第 1 大是升序的最后一个，下标 n-1
        target_index = n - k
        left, right = 0, n - 1  # 闭区间

        while True:
            i = self.partition(nums, left, right)
            if i == target_index:
                # 找到第 k 大元素
                return nums[i]
            if i > target_index:
                # 第 k 大元素在 [left, i - 1] 中
                right = i - 1
            else:
                # 第 k 大元素在 [i + 1, right] 中
                left = i + 1

    def findKthLargestHeap(self, nums: List[int], k: int) -> int:
        """
        使用最小堆的解法

        核心思路：
        维护一个大小为 k 的最小堆，堆顶就是第 k 大的元素。

        时间复杂度：O(n log k)
        空间复杂度：O(k)
        """
        import heapq

        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


# @lc code=end



#
# @lcpr case=start
# [3,2,1,5,6,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [3,2,3,1,2,4,5,5,6]\n4\n
# @lcpr case=end

#

if __name__ == "__main__":
    sol = Solution()

    # 测试用例 1：基本示例
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    result1 = sol.findKthLargest(nums1.copy(), k1)
    print(f"Test 1: findKthLargest([3,2,1,5,6,4], 2) = {result1}")
    assert result1 == 5, f"Expected 5, got {result1}"
    # 排序后：[1,2,3,4,5,6]，第 2 大是 5

    # 测试用例 2：有重复元素
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    result2 = sol.findKthLargest(nums2.copy(), k2)
    print(f"Test 2: findKthLargest([3,2,3,1,2,4,5,5,6], 4) = {result2}")
    assert result2 == 4, f"Expected 4, got {result2}"
    # 排序后：[1,2,2,3,3,4,5,5,6]，第 4 大是 4

    # 测试用例 3：k = 1（最大值）
    nums3 = [1, 2, 3, 4, 5]
    k3 = 1
    result3 = sol.findKthLargest(nums3.copy(), k3)
    print(f"Test 3: findKthLargest([1,2,3,4,5], 1) = {result3}")
    assert result3 == 5, f"Expected 5, got {result3}"

    # 测试用例 4：k = n（最小值）
    nums4 = [1, 2, 3, 4, 5]
    k4 = 5
    result4 = sol.findKthLargest(nums4.copy(), k4)
    print(f"Test 4: findKthLargest([1,2,3,4,5], 5) = {result4}")
    assert result4 == 1, f"Expected 1, got {result4}"

    # 测试用例 5：单个元素
    nums5 = [1]
    k5 = 1
    result5 = sol.findKthLargest(nums5.copy(), k5)
    print(f"Test 5: findKthLargest([1], 1) = {result5}")
    assert result5 == 1, f"Expected 1, got {result5}"

    # 测试用例 6：全部相同
    nums6 = [5, 5, 5, 5]
    k6 = 2
    result6 = sol.findKthLargest(nums6.copy(), k6)
    print(f"Test 6: findKthLargest([5,5,5,5], 2) = {result6}")
    assert result6 == 5, f"Expected 5, got {result6}"

    # 测试用例 7：堆解法测试
    nums7 = [3, 2, 1, 5, 6, 4]
    k7 = 2
    result7 = sol.findKthLargestHeap(nums7.copy(), k7)
    print(f"Test 7 (Heap): findKthLargestHeap([3,2,1,5,6,4], 2) = {result7}")
    assert result7 == 5, f"Expected 5, got {result7}"

    print("\nAll tests passed!")
