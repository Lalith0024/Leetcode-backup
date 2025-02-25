class Solution(object):
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        length = len(word)

        def helper(x, y, idx):
            if idx == length:
                return True
            if x < 0 or y < 0 or x >= rows or y >= cols or visited[x][y] or board[x][y] != word[idx]:
                return False

            visited[x][y] = True
            found = (helper(x + 1, y, idx + 1) or
                     helper(x, y + 1, idx + 1) or
                     helper(x - 1, y, idx + 1) or
                     helper(x, y - 1, idx + 1))
            visited[x][y] = False
            return found

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and helper(i, j, 0):
                    return True
        return False
        
