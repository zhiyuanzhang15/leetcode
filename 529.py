# 529. 扫雷游戏
# 中等
# 让我们一起来玩扫雷游戏！
# 给你一个大小为 m x n 二维字符矩阵 board ，表示扫雷游戏的盘面，其中：
# 'M' 代表一个 未挖出的 地雷，
# 'E' 代表一个 未挖出的 空方块，
# 'B' 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的 已挖出的 空白方块，
# 数字（'1' 到 '8'）表示有多少地雷与这块 已挖出的 方块相邻，
# 'X' 则表示一个 已挖出的 地雷。
# 给你一个整数数组 click ，其中 click = [clickr, clickc] 表示在所有 未挖出的 方块
# （'M' 或者 'E'）中的下一个点击位置（clickr 是行下标，clickc 是列下标）。
# 根据以下规则，返回相应位置被点击后对应的盘面：
# 如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X' 。
# 如果一个 没有相邻地雷 的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的 未挖出 方块都应该被递归地揭露。
# 如果一个 至少与一个地雷相邻 的空方块（'E'）被挖出，修改它为数字（'1' 到 '8' ），表示相邻地雷的数量。
# 如果在此次点击中，若无更多方块可被揭露，则返回盘面。
def updateBoard(board, click):
    def dfs(board,x,y):
        if board[x][y] != 'E':
            return 
        directions =[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        mines = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0<= nx < len(board) and 0 <= ny < len(board[0]) and board[nx][ny] == 'M':
                mines += 1
        if mines > 0:
            board[x][y] = str(mines)
        else:
            board[x][y] = 'B'
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0<= nx < len(board) and 0 <= ny < len(board[0]):
                    dfs(board,nx,ny)
    
    x,y = click
    if board[x][y] == 'M':
        board[x][y] = 'X'
    else:
        dfs(board,x,y)
    return board


board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]
click = [3,0]

print(updateBoard(board,click))
        

