class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dq = deque()
        
        ret = 0
        for r in range(row):
            for c in range(col):

                if grid[r][c] == 1:
                    dq.append((r,c))
                    grid[r][c] = 0

                    count = 1
                    while dq:
                        c_r, c_c = dq.popleft()
                        for rd, cd in ((1,0), (0,1), (-1, 0), (0,-1)):
                            n_r, n_c = rd + c_r, cd + c_c

                            if 0 <= n_r < row and 0 <= n_c < col and grid[n_r][n_c] != 0:
                                dq.append((n_r, n_c))
                                grid[n_r][n_c] = 0
                                count += 1
                    ret = max(ret, count)
        return ret