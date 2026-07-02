from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        R, C = len(grid), len(grid[0])
        
        # max_health[r][c] will store the maximum remaining health reaching grid[r][c]
        # Initialize with -1 (unvisited/unreachable)
        max_health = [[-1] * C for _ in range(R)]
        
        # Starting point health calculation
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False
            
        max_health[0][0] = start_health
        
        # Deque for 0-1 BFS / Standard BFS optimization
        # Stores elements as (row, col, current_health)
        queue = deque([(0, 0, start_health)])
        
        # Direction vectors for: top, right, bottom, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while queue:
            r, c, h = queue.popleft()
            
            # If we reached the bottom-right corner with positive health, we are done
            if r == R - 1 and c == C - 1:
                return True
                
            # If we found a better path to this cell since this item was queued, skip it
            if h < max_health[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries
                if 0 <= nr < R and 0 <= nc < C:
                    next_health = h - grid[nr][nc]
                    
                    # Only move if we stay alive AND it's a better path than found before
                    if next_health > 0 and next_health > max_health[nr][nc]:
                        max_health[nr][nc] = next_health
                        
                        # 0-1 BFS Optimization: 
                        # If no health is lost (grid cell is 0), prioritize it at the front.
                        # Otherwise, push it to the back.
                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc, next_health))
                        else:
                            queue.append((nr, nc, next_health))
                            
        return False
