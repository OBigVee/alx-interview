#!/usr/bin/python3
"""Island perimeter computing module.
"""
from typing import List

def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                i == n - 1 or (len(grid[i + 1]) > j and grid[i + 1][j] == 0),
                j == 0 or row[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
# def island_perimeter(grid: List[List[int]]) -> int:
#     """Island Perimeter"""
#     visit = set()

#     def dfs(i, j):
#         if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
#             return 1
#         if (i, j) in visit:
#             return 0

#         visit.add((i, j))
#         perimeter = dfs(i, j + 1)
#         perimeter += dfs(i + 1, j)
#         perimeter += dfs(i, j - 1)
#         perimeter += dfs(i - 1, j)
#         return perimeter

#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j]:
#                 return dfs(i, j)
