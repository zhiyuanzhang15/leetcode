# 208. 实现 Trie (前缀树)
# 中等
# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，
# 用于高效地存储和检索字符串数据集中的键。
# 这一数据结构有相当多的应用情景，例如自动补全和拼写检查。
# 请你实现 Trie 类：
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，
# 返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串
# word 的前缀之一为 prefix ，返回 true ；否则，返回 false

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# 示例使用
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))   # 输出: True
print(trie.search("app"))     # 输出: False
print(trie.startsWith("app")) # 输出: True
trie.insert("app")
print(trie.search("app"))     # 输出: True