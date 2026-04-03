#
# @lc app=leetcode.cn id=169 lang=python3
# @lcpr version=30204
#
# [169] 多数元素
#


# @lcpr-template-start
from typing import List

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    169. 多数元素 - Boyer-Moore 投票算法

    核心思想：
    多数元素是指在数组中出现次数大于 n/2 的元素。
    投票算法的核心：把不同的两两抵消，最后剩下的就是多数元素。

    算法流程：
    1. 维护一个候选者 candidate 和计数器 count
    2. 遍历数组：
       - 如果 count == 0，当前元素成为新的 candidate
       - 如果当前元素 == candidate，count += 1
       - 否则 count -= 1
    3. 最后 candidate 就是多数元素

    为什么正确？
    因为多数元素出现次数 > n/2，即使它和其他所有元素配对抵消，
    它仍然会剩下至少一个，所以最后幸存的一定是多数元素。

    时间复杂度：O(n)
    空间复杂度：O(1)
    """

    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


# @lc code=end


#
# @lcpr case=start
# [3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([1, 1, 1, 2, 2], 1),
        ([6, 5, 5], 5),
    ]

    print("多数元素 - 测试开始")
    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.majorityElement(nums)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: nums={nums} -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
