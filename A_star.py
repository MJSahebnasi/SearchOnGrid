from tree import Node
from matrix_stuff import get_neighbor_indices
import heapq


def my_manhattan_plus_heuristic(matrix, y, x, y_goal, x_goal):
    return min(abs(y_goal - y), min(y_goal, y) + len(matrix) - max(y_goal, y)) + min(abs(x_goal - x),
                                                                                     min(x_goal, x) + len(
                                                                                         matrix[0]) - max(x_goal, x))


def find_path(node, path):
    if node.father is None:
        path.reverse()
        return path
    path.append(node.dir_from_father)
    return find_path(node.father, path)


def update_children_gs(father):
    for child in father.children:
        if child.g >= father.g:
            child.g = father.g + 1
            update_children_gs(child)


def a_star(matrix, start_y, start_x, goal_y, goal_x):
    root = Node(start_y, start_x, None, None, 0, my_manhattan_plus_heuristic(matrix, start_y, start_x, goal_y, goal_x))
    open_list = [root]
    closed_list = []

    while len(open_list) > 0:
        heapq.heapify(open_list)
        current_node = heapq.heappop(open_list)

        if current_node.is_goal:
            return find_path(current_node, [])

        closed_list.append(current_node)

        for (child_y, child_x, dir) in get_neighbor_indices(matrix, current_node.position[0], current_node.position[1]):

            if matrix[child_y][child_x] != '1':

                new_g = current_node.g + 1
                child_is_closed = False

                child = next((node for node in open_list if node.position == (child_y, child_x)), None)

                if child is None:
                    child = next((node for node in closed_list if node.position == (child_y, child_x)), None)

                    # neither in closed nor in open:
                    if child is None:
                        child = Node(child_y, child_x, current_node, dir, new_g,
                                     my_manhattan_plus_heuristic(matrix, child_y, child_x, goal_y, goal_x),
                                     matrix[child_y][child_x] == 'A')
                        open_list.append(child)
                        current_node.children.add(child)

                    # child in closed-list:
                    else:
                        if child.g > new_g:
                            child.father = current_node
                            current_node.children.add(child)
                            child.g = new_g
                            update_children_gs(child)

                # child in open-list:
                else:
                    if child.g > new_g:
                        child.father = current_node
                        current_node.children.add(child)
                        child.g = new_g

                    if child_is_closed:
                        open_list.append(child)

                current_node.children.add(child)

    return []
