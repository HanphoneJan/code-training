#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30204
#
# [20] 有效的括号
# 题目：给定一个只包含括号的字符串，判断括号是否有效匹配
#

# @lcpr-template-start
# @lcpr-template-end

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """
        核心思想：栈（后进先出）

        括号匹配的规则：
        - 每个左括号必须与一个同类型的右括号匹配
        - 左括号必须以正确的顺序闭合（最近未匹配的左括号优先匹配）

        为什么用栈？
        栈的特性是"后进先出"，正好符合括号匹配的规则：
        - 遇到左括号，压入栈（等待匹配）
        - 遇到右括号，与栈顶的左括号匹配
        - 如果匹配成功，弹出栈顶；如果失败，说明无效

        时间复杂度：O(n)，每个字符只遍历一次
        空间复杂度：O(n)，最坏情况下栈需要存储所有左括号
        """
        # 用列表模拟栈
        stack = list()

        # 定义左括号和右括号
        left = ['(', '[', '{']
        right = [')', ']', '}']

        # 创建映射：右括号 -> 对应的左括号
        # 这样方便快速查找某个右括号应该匹配什么左括号
        pair_map = dict(zip(right, left))

        for char in s:
            # ========== 情况1：遇到左括号 ==========
            if char in left:
                # 压入栈，等待后续的右括号来匹配
                stack.append(char)

            # ========== 情况2：遇到右括号 ==========
            else:
                # 检查两个失败条件：
                # 1. 栈为空：没有左括号可以匹配，比如 ")(" 的第一个字符
                # 2. 栈顶与当前右括号不匹配：比如 "(]"
                if len(stack) == 0 or stack.pop() != pair_map[char]:
                    return False

        # ========== 最终检查 ==========
        # 如果栈不为空，说明有左括号没有被匹配，比如 "(()"
        # 只有当栈为空时，才说明所有括号都匹配成功
        return len(stack) == 0


# ========== 示例推演：s = "([])" ==========
#
# 初始：stack = []
#
# char='('：左括号，入栈，stack = ['(']
# char='['：左括号，入栈，stack = ['(', '[']
# char=']'：右括号，stack.pop()='['，pair_map[']']='['，匹配成功！stack = ['(']
# char=')'：右括号，stack.pop()='('，pair_map[')']='('，匹配成功！stack = []
#
# 遍历结束，stack 为空，返回 True
#
# ========== 示例：s = "([)]" ==========
#
# char='('：入栈，stack = ['(']
# char='['：入栈，stack = ['(', '[']
# char=')'：右括号，stack.pop()='['，但 pair_map[')']='('，'[' != '('，不匹配！
# 返回 False
# @lc code=end


# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
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
        ("() -> True",     lambda: sol.isValid("()"),     True),
        ("()[]{} -> True", lambda: sol.isValid("()[]{}"), True),
        ("(] -> False",    lambda: sol.isValid("(]"),     False),
        ("([]) -> True",   lambda: sol.isValid("([])"),   True),
        ("([)] -> False",  lambda: sol.isValid("([)]"),   False),
        ("{[] -> False",   lambda: sol.isValid("{[]"),    False),
        ("空串 -> True",    lambda: sol.isValid(""),       True),
    ])
