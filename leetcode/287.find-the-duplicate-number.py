#
# @lc app=leetcode.cn id=287 lang=python3
# @lcpr version=30204
#
# [287] 寻找重复数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    """
    287. 寻找重复数 - Floyd 判圈算法（龟兔赛跑算法）

    问题分析：
    数组有 n+1 个整数，范围在 [1, n] 之间，必有一个重复数。
    关键约束：不能修改数组，只能使用 O(1) 额外空间。

    核心洞察：
    将数组看作一个链表：下标 i 指向 nums[i]。
    由于存在重复数，这个"链表"必然存在环！
    - 每个下标 i 有一条出边指向 nums[i]
    - 重复数意味着有两个下标指向同一个值，形成环的入口

    Floyd 判圈算法（同 142. 环形链表 II）：
    1. 阶段一：快慢指针找相遇点
       - 慢指针每次走 1 步：slow = nums[slow]
       - 快指针每次走 2 步：fast = nums[nums[fast]]
       - 有环则必然相遇

    2. 阶段二：找环的入口（即重复数）
       - 一个指针从起点出发，另一个从相遇点出发
       - 两者每次各走 1 步，再次相遇点即为环入口

    数学证明：
    设环前长度为 a，环长度为 b。
    快慢指针相遇时，快指针比慢指针多走了 n 圈：2d = d + nb
    因此 d = nb，即慢指针走了 nb 步。
    从起点再走 a 步就到环入口，从相遇点再走 a 步也到环入口。

    时间复杂度: O(n) - 快慢指针最多遍历 2n 个元素
    空间复杂度: O(1) - 只使用两个指针
    """

    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd 判圈算法寻找重复数
        将数组看作链表：下标 i -> nums[i]
        """
        # 阶段一：快慢指针找相遇点
        # 选择 0 作为起点，因为数组元素范围是 [1, n]，0 一定不在环上
        slow = fast = 0
        while True:
            slow = nums[slow]           # 慢指针走 1 步
            fast = nums[nums[fast]]     # 快指针走 2 步
            if fast == slow:            # 相遇，找到环内一点
                break

        # 阶段二：找环的入口（重复数）
        # 数学结论：从起点和相遇点各走一步，再次相遇即为环入口
        head = 0
        while slow != head:
            slow = nums[slow]   # 从相遇点出发，每次 1 步
            head = nums[head]   # 从起点出发，每次 1 步

        return slow  # 环的入口就是重复数

# @lc code=end



#
# @lcpr case=start
# [1,3,4,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3,3,3]\n
# @lcpr case=end

#


if __name__ == "__main__":
    sol = Solution()

    # 测试用例: (nums, expected)
    tests = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([3, 3, 3, 3, 3], 3),
        ([1, 1], 1),
        ([2, 2, 2, 2, 2], 2),
    ]

    for nums, expected in tests:
        result = sol.findDuplicate(nums)
        print(f"nums={nums}, result={result}, expected={expected}, {'✓ PASS' if result == expected else '✗ FAIL'}")
