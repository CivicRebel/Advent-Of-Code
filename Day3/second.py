inFile = open("input.in", "r")


def get_steps(moves, intersection):
    steps_to_intersection = dict()
    total_steps = 0
    point_x = 0
    point_y = 0

    for j in moves:
        move = j[0]
        steps = int(j[1:])

        if move == "R":
            while steps > 0:
                steps -= 1
                total_steps += 1
                point_x += 1
                if (point_x, point_y) in intersection:
                    steps_to_intersection[(point_x, point_y)] = total_steps

        if move == "L":
            while steps > 0:
                steps -= 1
                point_x -= 1
                total_steps += 1
                if (point_x, point_y) in intersection:
                    steps_to_intersection[(point_x, point_y)] = total_steps

        if move == "U":
            while steps > 0:
                steps -= 1
                point_y += 1
                total_steps += 1
                if (point_x, point_y) in intersection:
                    steps_to_intersection[(point_x, point_y)] = total_steps

        if move == "D":
            while steps > 0:
                steps -= 1
                point_y -= 1
                total_steps += 1
                if (point_x, point_y) in intersection:
                    steps_to_intersection[(point_x, point_y)] = total_steps

    return steps_to_intersection
