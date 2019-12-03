from math import inf, fabs
from second import *

inFile = open("input.in", "r")


def read_wire_directions(file):
    line = inFile.readline()
    path_moves = []

    for i in line.split(","):
        path_moves.append(i)

    return path_moves


def get_points(moves):
    points_in_path = set()

    point_x = 0
    point_y = 0

    for j in moves:
        move = j[0]
        steps = int(j[1:])

        if move == "R":
            while steps > 0:
                steps -= 1
                point_x += 1
                points_in_path.add((point_x, point_y))

        if move == "L":
            while steps > 0:
                steps -= 1
                point_x -= 1
                points_in_path.add((point_x, point_y))

        if move == "U":
            while steps > 0:
                steps -= 1
                point_y += 1
                points_in_path.add((point_x, point_y))

        if move == "D":
            while steps > 0:
                steps -= 1
                point_y -= 1
                points_in_path.add((point_x, point_y))

    return points_in_path


first_wire_directions = read_wire_directions(inFile)
second_wire_directions = read_wire_directions(inFile)
first_path_points = get_points(first_wire_directions)
second_path_points = get_points(second_wire_directions)

intersection_points = first_path_points.intersection(second_path_points)

min_distance = inf

for i in intersection_points:
    min_distance = min(min_distance, fabs(i[0]) + fabs(i[1]))

min_distance = int(min_distance)

print(min_distance)

first_wire_values = get_steps(first_wire_directions, intersection_points)
second_wire_values = get_steps(second_wire_directions, intersection_points)

min_steps_value = inf

for i in intersection_points:
    if min_steps_value > first_wire_values[i] + second_wire_values[i]:
        min_steps_value = first_wire_values[i] + second_wire_values[i]

print(min_steps_value)