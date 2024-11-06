# 1263. 推箱子
# 困难
# 「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。
# 游戏地图用大小为 m x n 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。
# 现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ：
# 玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
# 地板用字符 '.' 表示，意味着可以自由行走。
# 墙用字符 '#' 表示，意味着障碍物，不能通行。 
# 箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。
# 玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
# 玩家无法越过箱子。
# 返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。

from collections import deque

def minPushBox(grid):
    m, n = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def is_valid(x,y):
        return 0 <= x < m and 0 <= y < n and grid[x][y] != '#'
    
    def can_reach(sx, sy, tx, ty, bx, by):
        queue = deque([(sx, sy)])
        visited = set((sx, sy))
        while queue:
            x, y = queue.popleft()
            if (x,y) == (tx,ty):
                return True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if is_valid(nx, ny) and (nx, ny) not in visited and (nx, ny) != (bx, by):
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        return False
    
    sx = sy = bx = by = tx = ty = -1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'S':
                sx, sy = i, j
            if grid[i][j] == 'B':
                bx, by = i, j
            if grid[i][j] == 'T':
                tx, ty = i, j
    
    queue = deque([(sx, sy, bx, by, 0)])
    visited = set((sx, sy, bx, by))

    while queue:
        sx, sy, bx, by, pushes = queue.popleft()
        if (bx, by) == (tx, ty):
            return pushes
        for dx, dy in directions:
            nbx, nby = bx + dx, by + dy
            nsx, nsy = bx - dx, by - dy
            if is_valid(nbx, nby) and is_valid(nsx, nsy) and can_reach(sx, sy, nsx, nsy, bx, by):
                if (nsx, nsy, nbx, nby) not in visited:
                    visited.add((nsx, nsy, nbx, nby))
                    queue.append((nsx, nsy, nbx, nby, pushes + 1))
    return -1

grid = [["#","#","#","#","#","#"],
             ["#","T",".",".","#","#"],
             ["#",".","#","B",".","#"],
             ["#",".",".",".",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]

print(minPushBox(grid))
