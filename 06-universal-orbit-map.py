filepath = "input/06.txt"

direct = dict()
indirect = dict()


def check_object(moon):
    global direct
    global indirect

    if not moon in direct.keys():
        direct[moon] = ["NULL", set()]
    if not moon in indirect.keys():
        indirect[moon] = [set(), set()]


def orbit(planet, moon):
    global direct
    global indirect
    check_object(planet)
    check_object(moon)

    direct[moon][0] = planet
    direct[planet][1].add(moon)

    indirect[planet][1].add(moon)
    indirect[planet][1] = indirect[planet][1].union(indirect[moon][1])
    for sun in indirect[planet][0]:
        indirect[sun][1] = indirect[sun][1].union(indirect[planet][1])
    indirect[moon][0].add(planet)
    indirect[moon][0] = indirect[moon][0].union(indirect[planet][0])
    for asteroid in indirect[moon][1]:
        indirect[asteroid][0] = indirect[asteroid][0].union(indirect[moon][0])


with open(filepath) as fp:
    line = fp.readline()
    while line:
        planet, moon = line.split(")")
        planet = planet.strip()
        moon = moon.strip()
        orbit(planet, moon)
        line = fp.readline()

count = 0
for moon in indirect.keys():
    count += len(indirect[moon][0])
    count += len(indirect[moon][1])
count = int(count / 2)

print("Part One:", count)


def get_path(moon):
    path = []
    planet = direct[moon][0]
    while planet != "NULL":
        path.insert(0, planet)
        planet = direct[planet][0]
    return path


path_you = get_path("YOU")
path_san = get_path("SAN")
while path_you[0] == path_san[0]:
    path_you.pop(0)
    path_san.pop(0)

print("Part Two:", len(path_you) + len(path_san))
