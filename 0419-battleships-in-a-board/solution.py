class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    board[i][j] = '.'
                    res += 1
                    for dy, dx in [(0, 1), (1, 0)]:
                        y = i + dy
                        x = j + dx
                        while y < m and x < n and board[y][x] == 'X':
                            board[y][x] = '.'
                            y += dy
                            x += dx

        return res
