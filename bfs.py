from collections import deque
from matrix_stuff import get_neighbor_indices


def bfs(matrix, start_y, start_x):
    que = deque()
    que.append((start_y, start_x, []))

    visited = [[False] * len(matrix[0]) for _ in range(len(matrix[0]))]
    visited[start_y][start_x] = True

    while len(que) > 0:
        y, x, path = que.popleft()

        for next_y, next_x, dir in get_neighbor_indices(matrix, y, x):

            if matrix[next_y][next_x] == 'A':
                path.append(dir)
                return path

            if not visited[next_y][next_x] and matrix[next_y][next_x] == '0':
                que.append((next_y, next_x, path + [dir]))
                visited[next_y][next_x] = True

    return []
