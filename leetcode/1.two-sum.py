#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30204
#
# [1] 两数之和
#


# 可运行测试用例
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # (nums, target, expected_indices)
        ([2, 7, 11, 15], 9, [0, 1]),  # 2 + 7 = 9
        ([3, 2, 4], 6, [1, 2]),  # 2 + 4 = 6
        ([3, 3], 6, [0, 1]),  # 3 + 3 = 6
        ([1, 3, 4, 8], 7, [1, 2]),  # 3 + 4 = 7
        ([-1, -2, -3, -4], -6, [1, 3]),  # 负数情况
    ]

    print("=" * 50)
    print("两数之和 - 测试开始")
    print("=" * 50)

    for i, (nums, target, expected) in enumerate(tests, 1):
        result = sol.twoSum(nums, target)
        # 由于答案可能有两种顺序，检查结果是否匹配（不考虑顺序）
        passed = sorted(result) == sorted(expected)
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"\n测试 {i}:")
        print(f"  输入: nums = {nums}, target = {target}")
        print(f"  输出: {result}")
        print(f"  期望: {expected}")
        print(f"  结果: {status}")

    print("\n" + "=" * 50)
    print("测试结束")
    print("=" * 50) @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    """
    两数之和 - 哈希表解法

    核心思路：
    - 遍历数组时，使用哈希表记录每个数值对应的索引
    - 对于当前元素num，检查(target - num)是否在哈希表中
    - 如果在，说明找到了答案；如果不在，将当前元素存入哈希表

    为什么用哈希表：
    - 哈希表的查找时间复杂度是O(1)
    - 将整体时间复杂度从O(n²)降低到O(n)

    时间复杂度：O(n) - 只需遍历数组一次
    空间复杂度：O(n) - 哈希表最多存储n个元素
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 哈希表：存储数值到索引的映射
        hashtable = dict()

        for i, num in enumerate(nums):
            # 计算需要找到的补数
            complement = target - num

            # 如果补数已在哈希表中，返回两个索引
            if complement in hashtable:
                return [hashtable[complement], i]

            # 将当前数值和索引存入哈希表
            hashtable[num] = i

        return []  # 题目保证有解，这里为了语法完整

# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

