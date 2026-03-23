#
# @lc app=leetcode.cn id=146 lang=python3
# @lcpr version=30204
#
# [146] LRU 缓存
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class LRUCache:
    """
    LRU (Least Recently Used) 缓存机制

    核心思想：
    1. 使用哈希表 O(1) 查找
    2. 使用双向链表维护访问顺序，头部是最近使用的，尾部是最久未使用的
    3. get 和 put 操作都需要将节点移到头部（标记为最近使用）

    双向链表优势：
    - 删除节点不需要知道前驱节点（有 prev 指针）
    - 在头部/尾部插入删除都是 O(1)

    结构：
    HashMap: key -> ListNode(key, value)
    DoublyLinkedList: head <-> node1 <-> node2 <-> ... <-> tail
    """

    class DLinkedNode:
        """双向链表节点"""
        def __init__(self, key: int = 0, value: int = 0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.cache = {}  # 哈希表：key -> DLinkedNode
        self.capacity = capacity
        self.size = 0

        # 使用伪头部和伪尾部节点，简化边界处理
        # 初始状态：head <-> tail
        self.head = self.DLinkedNode()
        self.tail = self.DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: 'LRUCache.DLinkedNode') -> None:
        """从双向链表中移除指定节点"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node: 'LRUCache.DLinkedNode') -> None:
        """将节点添加到头部（最近使用）"""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node: 'LRUCache.DLinkedNode') -> None:
        """将节点移到头部（标记为最近使用）"""
        self._remove_node(node)
        self._add_to_head(node)

    def _pop_tail(self) -> 'LRUCache.DLinkedNode':
        """移除尾部节点（最久未使用），返回该节点"""
        node = self.tail.prev
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        """
        获取key对应的值
        1. 如果不存在，返回-1
        2. 如果存在，将节点移到头部（标记最近使用），返回value
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        # 移动到头部（最近使用）
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        插入或更新key-value
        1. 如果key已存在，更新value，并移到头部
        2. 如果key不存在，创建新节点
           - 如果容量已满，移除尾部节点（最久未使用），再插入新节点
           - 如果容量未满，直接插入到头部
        """
        if key in self.cache:
            # 更新已有节点
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # 创建新节点
            new_node = self.DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            self.size += 1

            # 检查容量
            if self.size > self.capacity:
                # 移除最久未使用的节点（尾部）
                tail_node = self._pop_tail()
                del self.cache[tail_node.key]
                self.size -= 1
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end



if __name__ == "__main__":
    # 测试用例1: 基本操作
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"get(1) = {cache.get(1)}")  # 返回 1
    cache.put(3, 3)  # 该操作会使得 key 2 被删除
    print(f"get(2) = {cache.get(2)}")  # 返回 -1
    cache.put(4, 4)  # 该操作会使得 key 1 被删除
    print(f"get(1) = {cache.get(1)}")  # 返回 -1
    print(f"get(3) = {cache.get(3)}")  # 返回 3
    print(f"get(4) = {cache.get(4)}")  # 返回 4
