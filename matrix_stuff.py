import copy

def read_matrix():
    try:
        file = open('matrix.txt')
    except FileNotFoundError:
        print('file not found')
        return

    whole_thing = file.read()
    # print(whole_thing)
    input_lines = whole_thing.split('\n')
    # print('\n', input_lines)

    input_matrix = [[digit for digit in line.split(" ")] for line in input_lines]
    # print(input_matrix)

    file.close()
    return input_matrix


def get_neighbor_indices(grid, y, x):
    return [((y - 1) % len(grid), x, 'Up'), ((y + 1) % len(grid), x, 'Down'), (y, (x - 1) % len(grid[0]), 'Left'),
            (y, (x + 1) % len(grid[0]), 'Right')]


def find_index(matrix, v):
    for row, col in enumerate(matrix):
        if v in col:
            return row, col.index(v)


def draw_path(grid, path, start_y, start_x):
    matrix = copy.deepcopy(grid)
    y = start_y
    x = start_x
    for dir in path:
        if dir == 'Up':
            matrix[y][x] = 'U'
            y = (y - 1) % len(matrix)
        elif dir == 'Down':
            matrix[y][x] = 'D'
            y = (y + 1) % len(matrix)
        elif dir == 'Left':
            matrix[y][x] = 'L'
            x = (x - 1) % len(matrix[0])
        else:
            matrix[y][x] = 'R'
            x = (x + 1) % len(matrix[0])

    print()
    for row in matrix:
        print(row)
