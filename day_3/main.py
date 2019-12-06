file = open('./input.txt', 'r')
threads = file.readlines()
file.close()

thread1 = threads[0].split(',')
thread2 = threads[1].split(',')
thread1 = 'R8,U5,L5,D3'.split(',')
thread2 = 'U7,R6,D4,L4'.split(',')
thread1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'.split(',')
thread2 = 'U62,R66,U55,R34,D71,R55,D58,R83,U0'.split(',')
intersections = []
previous_x_start_a = 0
previous_y_start_a = 0
previous_x_start_b = 0
previous_y_start_b = 0


def cross_product(p1, p2):
    return p1[0] * p2[1] - p2[0] * p1[1]


def subtract(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]


def direction(p1, p2, p3):
    return cross_product(subtract(p3, p1), subtract(p2, p1))


def on_segment(start_a, end_a, p):
    return min(start_a[0], end_a[0]) <= p[0] <= max(start_a[0], end_a[0]) and min(start_a[1], end_a[1]) <= p[1] <= max(
        start_a[1], end_a[1])


def intersect(start_a, end_a, start_b, end_b):
    if (start_a[0] == end_a[0]) and (start_b[1] <= start_a[1] <= end_b[1]):
        return True
    elif (start_a[1] == start_a[1]) and (start_a[0] <= start_b[0] <= start_a[0]):
        return True
    else:
        return False


for i in range(len(thread1)):
    x_start_a = previous_x_start_a
    y_start_a = previous_y_start_a
    x_start_b = previous_x_start_b
    y_start_b = previous_y_start_b
    x_end_a = x_start_a
    y_end_a = y_start_a
    x_end_b = x_start_b
    y_end_b = y_start_b

    if thread1[i][0] == 'R':
        x_end_a += int(thread1[i][1:])
    elif thread1[i][0] == 'L':
        x_end_a -= int(thread1[i][1:])
    elif thread1[i][0] == 'D':
        y_end_a -= int(thread1[i][1:])
    elif thread1[i][0] == 'U':
        y_end_a += int(thread1[i][1:])

    if thread2[i][0] == 'R':
        x_end_b += int(thread2[i][1:])
    elif thread2[i][0] == 'L':
        x_end_b -= int(thread2[i][1:])
    elif thread2[i][0] == 'D':
        y_end_b -= int(thread2[i][1:])
    elif thread2[i][0] == 'U':
        y_end_b += int(thread2[i][1:])

    previous_x_start_a = x_end_a
    previous_y_start_a = y_end_a
    previous_x_start_b = x_end_b
    previous_y_start_b = y_end_b

    start_a, end_a, start_b, end_b = (x_start_a, y_start_a), (x_end_a, y_end_a), (x_start_b, y_start_b), (
        x_end_b, y_end_b)
    if intersect(start_a, end_a, start_b, end_b) or intersect(end_a, start_a, start_a, end_a):
        # print('intersects on: {}{} {}{}'.format(start_a, end_a, start_b, end_b))
        if start_a[0] == end_a[0]:
            x = start_a[0]
        else:
            x = start_b[0]

        if start_a[1] == end_a[1]:
            y = start_a[1]
        else:
            y = start_b[1]
        if x + y != 0:
            intersections.append(x + y)
        # print('({},{})'.format(x, y))

print(min(intersections))
