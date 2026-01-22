class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])

        # Directions to check 8 neighbors
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]

        # Step 1: Mark changes using temporary states
        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                # Count live neighbors
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < m and 0 <= nj < n:
                        # 1 or -1 means cell was alive
                        if abs(board[ni][nj]) == 1:
                            live_neighbors += 1

                # Rule 1 & 3: Live cell dies
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1   # alive → dead

                # Rule 4: Dead cell becomes alive
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2    # dead → alive

        # Step 2: Finalize the board
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1

