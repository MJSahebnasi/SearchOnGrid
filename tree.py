# for a_star_class
class Node:

    def __init__(self, y, x, father, dir_from_father, g, h, is_goal=False):
        self.position = (y, x)
        self.father = father
        self.g = g
        self.h = h
        self.is_goal = is_goal
        self.children = set()
        self.dir_from_father = dir_from_father

    def __lt__(self, other):
        return self.g + self.h < other.g + other.h
