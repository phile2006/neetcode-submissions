class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        dq = deque()
        count = 0

        for row in range(r):
            for col in range(c):

                if grid[row][col] == "1":
                    dq.append((row, col))
                    grid[row][col] = "0"
                    count += 1
                
                    while dq:
                        current_row, current_col = dq.popleft()
                        for row_dir, col_dir in ((0,1), (1,0), (0,-1), (-1,0)):
                            n_row, n_col = current_row + row_dir, current_col+  col_dir

                            if 0 <= n_row < r and 0 <= n_col < c and grid[n_row][n_col] != "0":
                                dq.append((n_row, n_col))
                                grid[n_row][n_col] = "0"
                
        return count