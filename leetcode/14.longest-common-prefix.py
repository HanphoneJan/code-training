#
# @lc app=leetcode.cn id=14 lang=python3
# @lcpr version=30204
#
# [14] 最长公共前缀
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        核心思想：以第一个字符串为基准，逐列比较所有字符串的同一位置字符

        策略：
        - 取 strs[0] 的第 i 个字符作为基准
        - 遍历所有字符串，检查第 i 个字符是否相同
        - 如果某字符串第 i 个字符不同，或已到达末尾，直接返回当前前缀

        时间复杂度：O(m*n)，m 是最短字符串长度，n 是字符串数量
        空间复杂度：O(1)
        """
        # 边界：空列表无公共前缀
        if not strs:
            return ""
        ans = ""
        i = 0
        # 注意：用 while True 而非 for 是为了手动控制退出时机
        # （更清晰的写法可以直接遍历 strs[0] 的每个字符）
        while True:
            # 取第一个字符串的第 i 个字符作为比较基准
            if i < len(strs[0]):
                word = strs[0][i]
            # 逐一检查所有字符串的第 i 个位置
            for str in strs:
                # 终止条件1：某字符串已到末尾（长度不足 i+1）
                # 终止条件2：某字符串第 i 个字符与基准不匹配
                if i >= len(str) or str[i] != word:
                    return ans
            # 所有字符串的第 i 个字符都相同，加入公共前缀
            ans += strs[0][i]
            i += 1

            

# @lc code=end



#
# @lcpr case=start
# ["flower","flow","flight"]\n
# @lcpr case=end

# @lcpr case=start
# ["dog","racecar","car"]\n
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
    _run_tests([
        ('["flower","flow","flight"] -> fl',
         lambda: sol.longestCommonPrefix(["flower","flow","flight"]), "fl"),
        ('["dog","racecar","car"] -> ""',
         lambda: sol.longestCommonPrefix(["dog","racecar","car"]),    ""),
        ('["a"] -> a',
         lambda: sol.longestCommonPrefix(["a"]),                      "a"),
        ('["abc","abc","abc"] -> abc',
         lambda: sol.longestCommonPrefix(["abc","abc","abc"]),        "abc"),
    ])
