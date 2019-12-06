threads = open('./input.txt').readlines()
thread_a = threads[0].split(',')
thread_b = threads[1].split(',')

directions_x = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
directions_y = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def find_poinds(wire):
    # start at the O(0,0)
    x = 0
    y = 0
    length = 0
    found_points = {}

    # loop through every operation in the wire
    for op in wire:

        # direction is the first char
        d = op[0]
        # the rest of the string is the amount of steps
        steps = int(op[1:])

        # add every point the follows from the steps taken to a dictonary
        for i in range(steps):
            x += directions_x[d]
            y += directions_y[d]

            # length keeps track of the (absolute) length of the wire
            length += 1

            # if a found point is already in the dictionary the wire intersects itself
            # if the point is not yet in the dictionary add it
            if (x, y) not in found_points:
                found_points[(x, y)] = length

    return found_points


found_points_a = find_poinds(thread_a)
found_points_b = find_poinds(thread_b)
union = set(found_points_a.keys()) & set(found_points_b.keys())
part1 = min([abs(x) + abs(y) for (x, y) in union])
part2 = min([found_points_a[p] + found_points_b[p] for p in union])
print('part 1: {}, part 2: {}'.format(part1, part2))
