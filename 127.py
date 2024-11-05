# 127. 单词接龙
# 困难
# 字典 wordList 中从单词 beginWord 到 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：
# 每一对相邻的单词只差一个字母。
#  对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。
# 如果不存在这样的转换序列，返回 0 。
import collections

def ladderLength(beginWord, endWord, wordList):
    def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1
        
    def addEdge(word: str):
        addWord(word)
        id1 = wordId[word]
        chars = list(word)
        for i in range(len(chars)):
            tmp = chars[i]
            chars[i] = "*"
            newWord = "".join(chars)
            addWord(newWord)
            id2 = wordId[newWord]
            edge[id1].append(id2)
            edge[id2].append(id1)
            chars[i] = tmp

    wordId = dict()
    edge = collections.defaultdict(list)
    nodeNum = 0

    for word in wordList:
        addEdge(word)
    
    addEdge(beginWord)
    if endWord not in wordId:
        return 0
    
    dis = [float("inf")] * nodeNum
    beginId, endId = wordId[beginWord], wordId[endWord]
    dis[beginId] = 0

    que = collections.deque([beginId])
    while que:
        x = que.popleft()
        if x == endId:
            return dis[endId] // 2 + 1
        for it in edge[x]:
            if dis[it] == float("inf"):
                dis[it] = dis[x] + 1
                que.append(it)
    
    return 0
