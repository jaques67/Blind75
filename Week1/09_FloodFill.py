# https://leetcode.com/problems/flood-fill/
# 733. Flood Fill
# AlgoMonster - Matrix as Graph / BFS: https://algo.monster/problems/flood_fill
import time
from typing import List
from collections import deque


class Solution:
    def floodFill_bfs(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:  # 102ms
        num_rows, num_cols = len(image), len(image[0])

        def get_neighbours(coord, color):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, 1, 0, -1]

            for i in range(len(delta_row)):
                neighbour_row = row + delta_row[i]
                neighbour_col = col + delta_col[i]
                if 0 <= neighbour_row < num_rows and 0 <= neighbour_col < num_cols:
                    if image[neighbour_row][neighbour_col] == color:
                        yield neighbour_row, neighbour_col

        def bfs(root):
            queue = deque([root])
            visited = [[False for c in range(num_cols)] for r in range(num_rows)]
            r, c = root
            old_color = image[r][c]
            image[r][c] = color
            visited[r][c] = True

            while queue:
                node = queue.popleft()
                for neighbour in get_neighbours(node, old_color):
                    r, c = neighbour
                    if visited[r][c]:
                        continue
                    image[r][c] = color
                    queue.append(neighbour)
                    visited[r][c] = True

        bfs((sr, sc))
        return image

    def floodFill_dfs(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:  # 84ms

        # out of bounds of the matrix
        # visted node
        # not same color as source
        rows, cols = len(image), len(image[0])
        s_color = image[sr][sc]
        marked = [(sr, sc)]
        image[sr][sc] = color

        def dfs(r, c):
            stack = [(r, c)]
            while len(stack) > 0:
                r, c = stack.pop()

                for new_r, new_c in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
                        continue
                    if image[new_r][new_c] != s_color:
                        continue
                    if not (new_r, new_c) in marked:
                        # print(new_r, new_c)
                        image[new_r][new_c] = color
                        stack.append((new_r, new_c))
                        marked.append((new_r, new_c))

        dfs(sr, sc)
        return image


if __name__ == '__main__':
    tests = [
        [[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]],
        [[[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]]
    ]

    sol = Solution()
    start_time = time.perf_counter()
    for test in tests:
        output = sol.floodFill_bfs(test[0], test[1], test[2], test[3])
        # output = sol.floodFill_dfs(test[0], test[1], test[2], test[3])

        if output == test[4]:
            print(output)
        else:
            print(f"Error: expected {test[4]} but got {output} instead for {test[0]}:{test[1]}:{test[2]}:{test[3]}")

    end_time = time.perf_counter()
    total_time = (end_time - start_time) * 1000000
    print(f"It took {total_time}ms")
