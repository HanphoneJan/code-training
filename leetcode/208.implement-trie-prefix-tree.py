#
# @lc app=leetcode.cn id=208 lang=python3
# @lcpr version=30204
#
# [208] 实现 Trie (前缀树)
#

# @lcpr-template-start
# @lcpr-template-end
# @lc code=start
class TrieNode:
    """
    Trie 节点类

    属性：
        son: 子节点数组，大小为 26（假设只包含小写字母 a-z）
        end: 布尔值，表示是否有单词在此节点结束
    """
    __slots__ = ['son', 'end']

    def __init__(self):
        # son[i] 表示字符 chr(ord('a') + i) 对应的子节点
        self.son = [None] * 26
        self.end = False  # 标记是否有单词在此结束


class Trie:
    """
    实现 Trie (前缀树)

    问题描述：
    Trie（发音类似 "try"），又称前缀树或字典树，是一种有序树，用于保存关联数组，
    其中的键通常是字符串。与二叉查找树不同，键不是直接保存在节点中，
    而是由节点在树中的位置决定。

    核心思想：
    利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较。

    节点结构：
    - 每个节点包含 26 个子节点（假设只包含小写字母）
    - 每个节点标记是否有单词在此结束

    时间复杂度：
    - insert: O(m) - m 为单词长度
    - search: O(m)
    - startsWith: O(m)

    空间复杂度：O(26^n) 最坏情况，实际中共享前缀会节省空间
    """

    def __init__(self):
        """初始化 Trie，创建根节点"""
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        向前缀树中插入字符串 word

        过程：
        1. 从根节点开始
        2. 对于 word 中的每个字符，计算其在 son 数组中的索引
        3. 如果该字符对应的子节点不存在，创建新节点
        4. 移动到子节点，继续处理下一个字符
        5. 最后一个字符处理完后，标记 end = True
        """
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.son[idx] is None:  # 无路可走？
                cur.son[idx] = TrieNode()  # 那就造路！
            cur = cur.son[idx]
        cur.end = True  # 标记单词结束

    def _find(self, word: str) -> int:
        """
        辅助函数：查找 word 在前缀树中的状态

        返回：
            0: word 不存在（路径中断）
            1: word 是某个单词的前缀，但本身不是单词
            2: word 是一个完整的单词
        """
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if cur.son[idx] is None:  # 道不同，不相为谋
                return 0
            cur = cur.son[idx]
        # 走过同样的路
        return 2 if cur.end else 1

    def search(self, word: str) -> bool:
        """
        如果字符串 word 在前缀树中，返回 true；否则返回 false
        """
        return self._find(word) == 2

    def startsWith(self, prefix: str) -> bool:
        """
        如果之前已经插入的字符串 word 的前缀之一为 prefix，返回 true；
        否则返回 false
        """
        return self._find(prefix) != 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end



#

if __name__ == "__main__":
    # 测试用例 1：基本操作
    print("Test 1: Basic operations")
    trie = Trie()

    # 插入单词
    trie.insert("apple")
    print(f"Insert 'apple'")

    # 搜索单词
    result1 = trie.search("apple")
    print(f"search('apple') = {result1}")  # True
    assert result1 == True, f"Expected True, got {result1}"

    result2 = trie.search("app")
    print(f"search('app') = {result2}")  # False
    assert result2 == False, f"Expected False, got {result2}"

    # 检查前缀
    result3 = trie.startsWith("app")
    print(f"startsWith('app') = {result3}")  # True
    assert result3 == True, f"Expected True, got {result3}"

    # 插入新单词
    trie.insert("app")
    result4 = trie.search("app")
    print(f"Insert 'app', then search('app') = {result4}")  # True
    assert result4 == True, f"Expected True, got {result4}"

    # 测试用例 2：多个单词
    print("\nTest 2: Multiple words")
    trie2 = Trie()
    words = ["cat", "car", "card", "care", "careful"]
    for word in words:
        trie2.insert(word)
        print(f"Insert '{word}'")

    # 搜索测试
    assert trie2.search("cat") == True
    assert trie2.search("car") == True
    assert trie2.search("card") == True
    assert trie2.search("care") == True
    assert trie2.search("careful") == True
    assert trie2.search("ca") == False
    assert trie2.search("careless") == False
    print("All search tests passed!")

    # 前缀测试
    assert trie2.startsWith("ca") == True
    assert trie2.startsWith("car") == True
    assert trie2.startsWith("care") == True
    assert trie2.startsWith("caref") == True
    assert trie2.startsWith("d") == False
    assert trie2.startsWith("cart") == False
    print("All prefix tests passed!")

    # 测试用例 3：空字符串（边界情况）
    print("\nTest 3: Empty string")
    trie3 = Trie()
    trie3.insert("")
    assert trie3.search("") == True
    assert trie3.startsWith("") == True
    print("Empty string tests passed!")

    print("\nAll tests passed!")
