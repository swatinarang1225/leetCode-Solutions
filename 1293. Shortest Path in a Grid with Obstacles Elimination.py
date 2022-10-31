class Solution:
    def shortestPath(self, grid:       List[List[int]], k: int) -> int:
        q = deque([(0, 0, k, 0)])
        visited = set()
        while q:
            i, j, rest, steps = q.popleft()
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j, rest) not in visited:
                visited.add((i, j, rest))
                if grid[i][j] == 0:
                    q.append((i, j+1, rest, steps + 1))
                    q.append((i, j-1, rest, steps + 1))
                    q.append((i+1, j, rest, steps + 1))
                    q.append((i-1, j, rest, steps + 1))

                else:
                    if rest > 0:
                        q.append((i, j+1, rest-1, steps + 1))
                        q.append((i, j-1, rest-1, steps + 1))
                        q.append((i+1, j, rest-1, steps + 1))
                        q.append((i-1, j, rest-1, steps + 1))
                    
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return steps
        return -1  
