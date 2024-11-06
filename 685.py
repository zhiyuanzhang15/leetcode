# 685. 冗余连接 II
# 困难
# 在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，
# 所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都
# 有且只有一个父节点，而根节点没有父节点。
# 输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）
# 的树及一条附加的有向边构成。附加的边包含在 1 到 n 中的两个不同顶点间，
# 这条附加的边不属于树中已存在的边。
# 结果图是一个以边组成的二维数组 edges 。 
# 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，
# 其中 ui 是 vi 的一个父节点。
# 返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。
# 若有多个答案，返回最后出现在给定二维数组的答案。

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

def findRedundantDirectedConnection(edges):
    n = len(edges)
    uf = UnionFind(n + 1)
    parent = list(range(n + 1))
    candidate1 = candidate2 = None

    for u, v in edges:
        if parent[v] != v:
            candidate1 = (parent[v], v)
            candidate2 = [u, v]
            break
        parent[v] = u
    
    for u, v in edges:
        if [u, v] == candidate2:
            continue
        if uf.find(u) == uf.find(v):
            if candidate1:
                return candidate1
            return [u, v]
        uf.union(u, v)
    return candidate2

edges = [[1,2],[1,3],[2,3]]
print(findRedundantDirectedConnection(edges))