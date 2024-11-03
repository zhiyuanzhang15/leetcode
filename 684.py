# 684. 冗余连接
# 中等
# 树可以看成是一个连通且 无环 的 无向 图。
# 给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。
# 添加的边的两个顶点包含在 1 到 n 中间，
# 且这条附加的边不属于树中已存在的边。
# 图的信息记录于长度为 n 的二维数组 
# edges ，edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。
# 请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。
# 如果有多个答案，则返回数组 edges 中最后出现的那个。

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

def findRedundantConnection(edges):
    n = len(edges)
    uf = UnionFind(n + 1)  # 因为节点值是从 1 到 n，所以需要 n + 1 的大小
    res = []
    for u, v in edges:
        if uf.find(u) == uf.find(v):
            res.append([u, v])
        uf.union(u, v)
    print(res)
    return res[-1]

edges = [[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9],[10,11],[3,10]]
print(findRedundantConnection(edges))

