# 146. LRU 缓存
# 中等
# 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# 实现 LRUCache 类：
# LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；
# 如果不存在，则向缓存中插入该组 key-value 。
# 如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key, value): 
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) >= self.capacity:
                self._remove_tail()
            new_node = ListNode(key,value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
    
    def _add_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)
    
    def _remove_tail(self):
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        del self.cache[tail_node.key]

# 示例使用
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))  # 输出: 1
cache.put(3, 3)
print(cache.get(2))  # 输出: -1
cache.put(4, 4)
print(cache.get(1))  # 输出: -1
print(cache.get(3))  # 输出: 3
print(cache.get(4))  # 输出: 4