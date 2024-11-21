# 51. N 皇后
# 困难
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，
# 并且使皇后彼此之间不能相互攻击。
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，
# 该方案中 'Q' 和 '.' 分别代表了皇后和空位。

def solveNQueens(n):
    def backtrack(row):
        if row == n:
            board = [''.join(row) for row in board_state]
            result.append(board)
        for col in range(n):
            if col in cols or (row -col) in diag1 or (row + col) in diag2:
                continue
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board_state[row][col] = 'Q'
            backtrack(row + 1)
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            board_state[row][col] = '.'
    
    result = []
    cols = set()
    diag1 = set()
    diag2 = set()
    board_state = [['.'] * n for _ in range(n)]
    backtrack(0)
    return result

n = 4
solutions = solveNQueens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()