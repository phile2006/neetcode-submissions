class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #check each 0, add to queue and bfs from there
        c_row, c_col = len(grid) , len(grid[0])
        dq = deque()

        for i in range(c_row):
            for j in range(c_col ):
                if grid[i][j] == 0:
                    dq.append((i,j,0))
        
        while dq:
            r, c, count = dq.popleft()
            count += 1
            for d_r, d_c in ((0,1), (1,0), (-1,0), (0,-1)):
                n_r, n_c = r + d_r , c + d_c

                if 0 <= n_r < c_row and 0<= n_c < c_col and grid[n_r][n_c] == 2147483647 :
                    grid[n_r][n_c] =  count
                    dq.append((n_r, n_c, count))