#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30204
#
# [146] LRU 缓存
#

# @lcpr-template-start
from typing import Optional

# @lcpr-template-end
# @lc code=start
class Node:
    """
    双向链表节点。
    __slots__ 用于提高访问属性的速度，并节省内存。
    """
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value


class LRUCache:
    """
    146. LRU 缓存 - 哈希表 + 双向链表

    核心思想：
    LRU（Least Recently Used）缓存淘汰策略：当缓存满时，淘汰最久未使用的数据。
    需要两个数据结构配合：
    1. 哈希表（dict）：key -> Node，实现 O(1) 查找
    2. 双向链表：按使用顺序排列，头部是最新使用的，尾部是最久未使用的

    为什么用双向链表？
    - 删除节点和移动节点到头部都是 O(1)
    - 配合哈希表可以直接定位到要操作的节点

    操作流程：
    - get：命中则把节点移到链表头部，未命中返回 -1
    - put：如果 key 已存在，更新 value 并移到头部；
           如果 key 不存在，插入新节点到头部；
           如果容量超出，淘汰尾部节点。

    时间复杂度：get 和 put 都是 O(1)
    空间复杂度：O(capacity)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()  # 哨兵节点，构成循环双向链表
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}  # 哈希表：key -> Node

    # 获取 key 对应的节点，同时把该节点移到链表头部（表示最近使用）
    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:  # 没有这本书
            return None
        node = self.key_to_node[key]  # 有这本书
        self.remove(node)  # 把这本书抽出来
        self.push_front(node)  # 放到最上面
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)  # get_node 会把对应节点移到链表头部
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)  # get_node 会把对应节点移到链表头部
        if node:  # 有这本书
            node.value = value  # 更新 value
            return
        # 新书
        self.key_to_node[key] = node = Node(key, value)
        self.push_front(node)  # 放到最上面
        if len(self.key_to_node) > self.capacity:  # 书太多了
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # 去掉最后一本书

    # 删除一个节点（抽出一本书）
    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev

    # 在链表头添加一个节点（把一本书放到最上面）
    def push_front(self, x: Node) -> None:
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


if __name__ == "__main__":
    print("LRU 缓存 - 测试开始")

    # 测试 1
    print("测试 1:")
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"  get(1) = {cache.get(1)}, 期望 = 1")
    cache.put(3, 3)  # 淘汰 key 2
    print(f"  get(2) = {cache.get(2)}, 期望 = -1")
    cache.put(4, 4)  # 淘汰 key 1
    print(f"  get(1) = {cache.get(1)}, 期望 = -1")
    print(f"  get(3) = {cache.get(3)}, 期望 = 3")
    print(f"  get(4) = {cache.get(4)}, 期望 = 4")

    # 测试 2
    print("测试 2:")
    cache2 = LRUCache(1)
    cache2.put(2, 1)
    print(f"  get(2) = {cache2.get(2)}, 期望 = 1")
    cache2.put(3, 2)
    print(f"  get(2) = {cache2.get(2)}, 期望 = -1")
    print(f"  get(3) = {cache2.get(3)}, 期望 = 2")

    print("测试结束")
