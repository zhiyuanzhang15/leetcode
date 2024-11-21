# 994. 腐烂的橘子
# 中等
# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

from collections import deque

def orangesRotting(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r,c))
            elif grid[r][c] == 1:
                fresh_count += 1
    
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    minutes = 0

    while queue and fresh_count > 0:
        minutes += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny <= cols and grid[nx][ny] == '1':
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
                    fresh_count -= 1
    return minutes if fresh_count == 0 else -1
                

# 示例使用
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]

# 计算腐烂所有新鲜橘子所需的最小时间
result = orangesRotting(grid)
print(result)  # 输出: 4