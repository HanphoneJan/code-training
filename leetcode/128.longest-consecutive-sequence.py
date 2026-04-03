#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30204
#
# [128] 最长连续序列
#


# @lcpr-template-start
from typing import List

# @lcpr-template-end
# @lc code=start
class Solution:
    """
    128. 最长连续序列 - 哈希表

    核心思想：
    题目要求找出最长连续序列的长度，且时间复杂度要优于 O(n log n)（不能排序）。
    利用哈希集合 O(1) 查找的特性，以每个数字为起点，向右扩展序列。

    关键优化：
    不遍历所有数字作为起点，而是只从 "序列起点"（即 x-1 不在集合中的数字）开始。
    这样每个数字最多被访问两次（一次作为其他序列的内部元素被跳过，一次作为起点被遍历），
    总时间复杂度为 O(n)。

    时间复杂度：O(n)
    空间复杂度：O(n)，哈希集合
    """

    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)  # 把 nums 转成哈希集合，去重并支持 O(1) 查找
        ans = 0

        for x in st:  # 遍历哈希集合中的每个数字
            if x - 1 in st:  # 如果 x 不是序列的起点，直接跳过
                continue

            # x 是序列的起点，向右不断查找下一个连续数字
            y = x + 1
            while y in st:
                y += 1

            # 循环结束后，y-1 是最后一个在哈希集合中的数
            # 从 x 到 y-1 一共 y-x 个数
            ans = max(ans, y - x)

        return ans


# @lc code=end


#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([100, 4, 200, 1, 3, 2], 4),           # 1,2,3,4 长度为 4
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),   # 0,1,2,3,4,5,6,7,8 长度为 9
        ([1, 0, 1, 2], 3),                     # 0,1,2 长度为 3
        ([], 0),                               # 空数组
        ([1], 1),                              # 单个元素
        ([1, 2, 0, 1], 3),                     # 0,1,2 长度为 3
    ]

    print("最长连续序列 - 测试开始")
    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.longestConsecutive(nums)
        passed = result == expected
        status = "PASS" if passed else "FAIL"
        print(f"测试 {i}: nums={nums} -> {status}")
        if not passed:
            print(f"  输出: {result}")
            print(f"  期望: {expected}")
    print("测试结束")
