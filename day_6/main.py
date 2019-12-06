class Map:
    def __init__(self, orbits):
        self.map = dict()
        self.orbits = orbits
        self.orbits_required = 0
        self.path = []
        self.orbit_lenghts = dict()

        for orbit in orbits:
            if orbit[0] in self.map.keys():
                self.map[orbit[0]].append(orbit[1])
            else:
                self.map[orbit[0]] = [orbit[1]]

    def walk(self, key, steps):
        self.orbit_lenghts[key] = steps
        if key in self.map.keys():
            for k in self.map[key]:
                self.walk(k, steps + 1)

    def calculate_orbit_lenghts(self):
        self.walk('COM', 0)
        return sum(self.orbit_lenghts.values())

    def find_path_to_com(self, target):
        for planet, orbit in self.map.items():
            if target in orbit:
                self.path.append(planet)
                return self.find_path_to_com(planet)

        output = self.path.copy()
        output.reverse()
        self.path.clear()
        return output

    def find_path_between(self, start, target):
        path_to_start = self.find_path_to_com(start)
        path_to_target = self.find_path_to_com(target)

        count = 0
        for a, b in zip(path_to_start, path_to_target):
            if a != b:
                return len(path_to_start) - count + len(path_to_target) - count
            else:
                count += 1


file = open('./input.txt')
inputs = [o.strip().split(')') for o in file.readlines()]
file.close()
m = Map(inputs)
print('part1: {}'.format(m.calculate_orbit_lenghts()))
# print('part2: {}'.format(m.find_path_to_com('YOU')))
print(m.find_path_to_com('YOU'))
print(m.find_path_to_com('SAN'))
print(m.find_path_between('YOU', 'SAN'))
