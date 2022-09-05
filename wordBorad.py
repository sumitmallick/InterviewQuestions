def helper(board, word, cur, i, j, visited):
        if cur == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[cur]:
            return False

        visited[i][j] = True
        result = helper(board, word, cur + 1, i + 1, j, visited) or helper(board, word, cur + 1, i - 1, j, visited) or helper(board, word, cur + 1, i, j + 1, visited) or helper(board, word, cur + 1, i, j - 1, visited)
        visited[i][j] = False

        return result

def wordBoard(word, board):
    visited = [[False for j in range(len(board[0]))] for i in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if helper(board, word, 0, i, j, visited):
                return True

    return False

        
print(wordBoard("ADEE",  [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]))
# Output: True