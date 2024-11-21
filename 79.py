# 79. 单词搜索
# 中等
# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
# 如果 word 存在于网格中，返回 true ；否则，返回 false 。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，
# 其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母不允许被重复使用。

def exist(board, word):
    def dfs(board, word, i, j, k):
        if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        
        temp, board[i][j] = board[i][j], '/'
        res = (dfs(board, word, i + 1, j, k + 1) or
               dfs(board, word, i - 1, j, k + 1) or
               dfs(board, word, i , j + 1, k + 1) or
               dfs(board, word, i, j - 1, k + 1) )
        board[i][j] = temp
        return res
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, word, i, j, 0):
                return True
    return False

# 示例使用
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board, word))  # 输出: True