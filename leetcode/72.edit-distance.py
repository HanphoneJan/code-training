#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30204
#
# [72] 编辑距离
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from functools import cache

class Solution:
    """
    编辑距离（Edit Distance / Levenshtein Distance）

    定义：两个字符串之间，由一个转成另一个所需的最少编辑操作次数。
    允许的编辑操作：插入、删除、替换。

    应用场景：
    - 拼写检查（计算单词与词典中单词的编辑距离）
    - DNA序列比对（生物信息学）
    - 机器翻译和语音识别评价标准（BLEU等）
    - 版本控制（diff算法）
    """

    def minDistanceMem(self, word1: str, word2: str) -> int:
        """
        解法一：记忆化搜索（递归 + 缓存）

        核心思想：
        定义 dfs(i, j) = word1[0..i] 转换成 word2[0..j] 的最小编辑距离

        边界条件：
        - i < 0：word1为空，需要插入 j+1 个字符
        - j < 0：word2为空，需要删除 i+1 个字符

        状态转移：
        - 如果 s[i] == t[j]：不用操作，dfs(i, j) = dfs(i-1, j-1)
        - 否则，取三种操作的最小值 + 1：
          1. 删除：dfs(i-1, j) + 1（删除s[i]）
          2. 插入：dfs(i, j-1) + 1（在s末尾插入t[j]）
          3. 替换：dfs(i-1, j-1) + 1（将s[i]替换成t[j]）

        时间复杂度：O(n×m)，其中 n=len(word1), m=len(word2)
        空间复杂度：O(n×m)，递归栈 + 缓存
        """
        s, t = word1, word2
        n, m = len(s), len(t)

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            # 边界：word1 已用完，需要插入 j+1 个字符
            if i < 0:
                return j + 1
            # 边界：word2 已用完，需要删除 i+1 个字符
            if j < 0:
                return i + 1
            # 当前字符相同，不用操作，继续比较前面
            if s[i] == t[j]:
                return dfs(i - 1, j - 1)
            # 当前字符不同，取三种操作的最小值
            # dfs(i-1, j): 删除 s[i]
            # dfs(i, j-1): 插入 t[j] 到 s[i] 后面
            # dfs(i-1, j-1): 将 s[i] 替换为 t[j]
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1

        return dfs(n - 1, m - 1)

    def minDistance(self, word1: str, word2: str) -> int:
        """
        解法二：动态规划（二维数组）

        定义 dp[i][j]：
        word1 的前 i 个字符（即 word1[0..i-1]）
        转换成 word2 的前 j 个字符（即 word2[0..j-1]）
        所需的最小编辑距离

        为什么要预留 dp[0][j] 和 dp[i][0]？
        处理空字符串的情况：
        - dp[0][j] = j：空串变成 j 个字符，需要插入 j 次
        - dp[i][0] = i：i 个字符变成空串，需要删除 i 次

        状态转移方程：
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1]  # 字符相同，不需要操作
        else:
            dp[i][j] = min(
                dp[i-1][j],     # 删除 word1[i-1]
                dp[i][j-1],     # 插入 word2[j-1]
                dp[i-1][j-1]    # 替换 word1[i-1] 为 word2[j-1]
            ) + 1

        时间复杂度：O(n×m)
        空间复杂度：O(n×m)
        """
        n, m = len(word1), len(word2)

        # dp[i][j] 表示 word1[:i] 转换为 word2[:j] 的最小编辑距离
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # 初始化边界
        # dp[0][j]：空字符串变成 word2[:j]，需要 j 次插入
        dp[0] = list(range(m + 1))

        # dp[i][0]：word1[:i] 变成空字符串，需要 i 次删除
        for i in range(1, n + 1):
            dp[i][0] = i

        # 填充DP表
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 当前字符相同，继承之前的编辑距离
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 取三种操作的最小值
                    # dp[i-1][j]：删除 word1[i-1]
                    # dp[i][j-1]：在 word1[i-1] 后插入 word2[j-1]
                    # dp[i-1][j-1]：将 word1[i-1] 替换为 word2[j-1]
                    dp[i][j] = min(
                        dp[i - 1][j],    # 删除
                        dp[i][j - 1],    # 插入
                        dp[i - 1][j - 1] # 替换
                    ) + 1

        return dp[n][m]

    def minDistanceTwoArrays(self, word1: str, word2: str) -> int:
        """
        解法三：空间优化 - 滚动数组（两个一维数组）

        观察：dp[i][j] 只依赖于上一行和当前行的左边
        - dp[i-1][j]：上一行，同列
        - dp[i][j-1]：当前行，左列
        - dp[i-1][j-1]：上一行，左列

        因此只需要保存两行即可：
        - f[0]：上一行
        - f[1]：当前行

        用 (i+1) % 2 来切换当前行

        时间复杂度：O(n×m)
        空间复杂度：O(m)
        """
        n, m = len(word1), len(word2)

        # 两行数组，交替使用
        # prev: 上一行，curr: 当前行
        prev = list(range(m + 1))  # dp[0][*] = 0, 1, 2, ..., m
        curr = [0] * (m + 1)

        for i in range(1, n + 1):
            curr[0] = i  # dp[i][0] = i

            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 字符相同，使用对角线值
                    curr[j] = prev[j - 1]
                else:
                    # 取三种操作的最小值
                    curr[j] = min(
                        prev[j],      # 删除（来自上一行）
                        curr[j - 1],  # 插入（来自当前行左边）
                        prev[j - 1]   # 替换（来自对角线）
                    ) + 1

            # 交换两行，准备下一轮
            prev, curr = curr, prev

        # 注意：最后结果在 prev[m] 因为交换了
        return prev[m]

    def minDistanceOneArray(self, word1: str, word2: str) -> int:
        """
        解法四：空间优化 - 一个数组（最优空间）

        进一步优化：只用一维数组

        关键观察：
        dp[i-1][j-1]（对角线）在遍历过程中会被覆盖，需要额外变量保存

        变量设计：
        - f[j] 表示 dp[i-1][j]（上一行）
        - pre 表示 dp[i-1][j-1]（对角线，需要提前保存）

        遍历顺序：
        从左到右，对于每个 j：
        1. 先保存 f[j]（它将成为下一轮的对角线）
        2. 计算新的 f[j]

        时间复杂度：O(n×m)
        空间复杂度：O(m) - 最优
        """
        m = len(word2)

        # f[j] = word1[:i] 转换成 word2[:j] 的最小编辑距离
        f = list(range(m + 1))  # dp[0][j] = j

        for x in word1:
            pre = f[0]  # 保存对角线值 dp[i-1][j-1]
            f[0] += 1   # dp[i][0] = i+1，即删除次数加一

            for j, y in enumerate(word2):
                tmp = f[j + 1]  # 保存当前值，它将成为下一轮的对角线

                if x == y:
                    # 字符相同，使用对角线值
                    f[j + 1] = pre
                else:
                    # 取三种操作的最小值
                    # f[j+1]：删除（原值，来自上一行）
                    # f[j]：插入（已更新，来自当前行）
                    # pre：替换（对角线）
                    f[j + 1] = min(f[j + 1], f[j], pre) + 1

                pre = tmp  # 更新对角线值供下一轮使用

        return f[m]

# @lc code=end



#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#

