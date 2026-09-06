class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_r = len(grid)
        len_c = len(grid[0])

        def dfs(r, c):
            if r < 0 or r>= len_r or c < 0 or c >= len_c or grid[r][c] != "1":
                return
            
            grid[r][c] = -1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0

        for row in range(len_r):
            for col in range(len_c):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)

        return islands