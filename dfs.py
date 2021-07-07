from matrix_stuff import get_neighbor_indices


def dfs(matrix, start_y, start_x, visited, path):
    visited[start_y][start_x] = True

    for (y, x, dir) in get_neighbor_indices(matrix, start_y, start_x):

        if matrix[y][x] == 'A':
            path.append(dir)
            return True

        if matrix[y][x] == '0' and not visited[y][x]:
            path.append(dir)
            if dfs(matrix, y, x, visited, path):
                return True
            path.pop()

    return False
