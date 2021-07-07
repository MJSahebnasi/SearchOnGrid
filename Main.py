from bfs import bfs
from matrix_stuff import read_matrix, find_index, draw_path
from dfs import dfs
from A_star import a_star  # , a_star_wikiVersion
from collections import deque

matrix = read_matrix()
# print('primary map:')
# for row in matrix:
#     print(row)
# print()
(start_y, start_x) = find_index(matrix, 'S')

print('dfs:')
path = deque()
if dfs(matrix, start_y, start_x, [[False] * len(matrix[0]) for _ in range(len(matrix[0]))], path):
    for dir in path:
        print(dir, end=' ')
    # draw_path(matrix, path, start_y, start_x)
else:
    print('no path found!')

print('\nbfs:')
result = bfs(matrix, start_y, start_x)
if len(result) > 0:
    for dir in result:
        print(dir, end=' ')
    # draw_path(matrix, result, start_y, start_x)
else:
    print('no path found!')

print('\nA*:')
(goal_y, goal_x) = find_index(matrix, 'A')
# result = a_star_wikiVersion(matrix, start_y, start_x, goal_y, goal_x)
result = a_star(matrix, start_y, start_x, goal_y, goal_x)
if len(result) > 0:
    for dir in result:
        print(dir, end=' ')
    # draw_path(matrix, result, start_y, start_x)
else:
    print('no path found!')
