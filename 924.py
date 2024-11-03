# 924. 尽量减少恶意软件的传播
# 困难
# 给出了一个由 n 个节点组成的网络，用 n × n 个邻接矩阵图 graph 表示。
# 在节点网络中，当 graph[i][j] = 1 时，表示节点 i 能够直接连接到另一个节点 j。 
# 一些节点 initial 最初被恶意软件感染。
# 只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，
# 那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。
# 假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。
# 如果从 initial 中移除某一节点能够最小化 M(initial)， 
# 返回该节点。如果有多个节点满足条件，就返回索引最小的节点。
# 请注意，如果某个节点已从受感染节点的列表 initial 中删除，
# 它以后仍有可能因恶意软件传播而受到感染。

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

def minMalwareSpread(graph, initial):
    n = len(graph)
    uf = UnionFind(n)

    # 合并所有连通的节点
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                uf.union(i, j)

    # 计算每个连通分量的大小
    size = [0] * n
    for i in range(n):
        root = uf.find(i)
        size[root] += 1

    # 计算每个初始感染节点的影响
    impact = [0] * n
    for node in initial:
        root = uf.find(node)
        impact[root] += 1

    # 选择最优节点
    best_node = min(initial)
    max_reduction = 0
    for node in initial:
        root = uf.find(node)
        if impact[root] == 1:  # 只有一个初始感染节点
            if size[root] > max_reduction or (size[root] == max_reduction and node < best_node):
                max_reduction = size[root]
                best_node = node

    return best_node