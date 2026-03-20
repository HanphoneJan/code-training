#
# @lc app=leetcode.cn id=31 lang=python3
# @lcpr version=30204
#
# [31] 下一个排列
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        核心思想：三步法找下一个排列

        下一个排列的定义：字典序比当前排列大的最小排列。
        例如 [1,2,3] 的下一个是 [1,3,2]，[3,2,1] 的下一个是 [1,2,3]（循环）。

        三步法：
        1. 从右向左找第一个"下降点" i：nums[i] < nums[i+1]
           （说明 i 右边的子数组是降序的，交换 i 处的数字可以让排列变大）
        2. 从右向左找 i 右边最小的比 nums[i] 大的数 j，交换 nums[i] 和 nums[j]
           （交换后，排列在 i 处变大了，但要让整体尽可能小，所以选最小的大数）
        3. 反转 i+1 到末尾的部分（使其变为升序，得到最小的后缀）
        """
        n = len(nums)

        # 第一步：从右向左找第一个"下降点" i（nums[i] < nums[i+1]）
        # 数组右侧是降序的，找到第一个破坏降序的位置
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 如果找到下降点，执行第二步；否则整个数组是降序，直接跳到第三步反转整个数组
        if i >= 0:
            # 第二步：从右向左找 nums[i] 右边最小的比 nums[i] 大的数 nums[j]
            # 由于 i+1 到末尾是降序的，从右往左找到的第一个大于 nums[i] 的数就是最小的
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # 交换 nums[i] 和 nums[j]，使排列在 i 处变大
            nums[i], nums[j] = nums[j], nums[i]

        # 第三步：反转 i+1 到末尾的部分，使其从降序变为升序（得到最小的后缀）
        # 注意：若第一步未找到 i（整个数组降序），此时 i = -1，反转整个数组
        # 原地双指针反转，空间复杂度 O(1)
        # （不用 nums[i+1:] = nums[i+1:][::-1]，因为切片赋值会创建临时副本）
        left, right = i + 1, n - 1
        while left < right:  # 双指针从两端向中间交换，实现原地反转
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,5]\n
# @lcpr case=end

#


if __name__ == "__main__":
    import sys

    def _run_tests(cases):
        passed = 0
        for desc, func, expected in cases:
            try:
                got = func()
            except Exception as e:
                got = f"ERROR: {e}"
            ok = got == expected
            passed += ok
            print(f"  [{'PASS' if ok else 'FAIL'}] {desc}")
            if not ok:
                print(f"         Expected : {expected}")
                print(f"         Got      : {got}")
        print(f"\n  {passed}/{len(cases)} passed")
        sys.exit(0 if passed == len(cases) else 1)

    sol = Solution()

    def _next(arr):
        sol.nextPermutation(arr)
        return arr

    _run_tests([
        ("[1,2,3] -> [1,3,2]", lambda: _next([1,2,3]),   [1,3,2]),
        ("[3,2,1] -> [1,2,3]", lambda: _next([3,2,1]),   [1,2,3]),
        ("[1,1,5] -> [1,5,1]", lambda: _next([1,1,5]),   [1,5,1]),
        ("[1] -> [1]",         lambda: _next([1]),        [1]),
        ("[1,3,2] -> [2,1,3]", lambda: _next([1,3,2]),   [2,1,3]),
        ("[2,3,1] -> [3,1,2]", lambda: _next([2,3,1]),   [3,1,2]),
    ])
