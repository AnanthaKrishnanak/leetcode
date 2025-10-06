class Solution:
    def __init__(self):
        self.visited = set()

    def expand(self, grid, row, col):
        m, n = len(grid), len(grid[0])

        if (row, col) in self.visited or grid[row][col] != "1":
            return

        self.visited.add((row, col))

        if row > 0:
            self.expand(grid, row - 1, col)
        if row < m - 1:
            self.expand(grid, row + 1, col)
        if col > 0:
            self.expand(grid, row, col - 1)
        if col < n - 1:
            self.expand(grid, row, col + 1)

    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        self.visited = set()
        c = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "0" or (row, col) in self.visited:
                    continue
                c += 1
                self.expand(grid, row, col)

        return c
