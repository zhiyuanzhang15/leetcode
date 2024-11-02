# 200. 岛屿数量
# 中等
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。

def numIslands(grid):
    num_isIlands = 0
    def dfs(grid,r,c):
        if r < 0 or r>= len(grid) or c< 0 or c>= len(grid[0]) or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(grid,r-1,c)
        dfs(grid,r+1,c)
        dfs(grid,r,c-1)
        dfs(grid,r,c+1)
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                dfs(grid,i,j)
                num_isIlands += 1
    return num_isIlands
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(numIslands(grid))
