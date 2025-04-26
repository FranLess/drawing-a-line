import math
RANGO = 50

try:
    s_cord = input("Ingresa la primera coordenada [<x>,<y>]: ").rsplit(",")
    t_cord = input("Ingresa la segunda coordenada [<x>,<y>]: ").rsplit(",")
    S: tuple[int, int] = (int(s_cord[0]) - 1, int(s_cord[1]) - 1)
    T: tuple[int, int] = (int(t_cord[0]) - 1, int(t_cord[1]) - 1)
except ValueError as e:
    print("Debes ingresar dos valores de la forma x,y: ejemplo 5,6")
    raise ValueError(e)

if (S[0] > RANGO) or (S[1] > RANGO) or (T[0] > RANGO) or (T[1] > RANGO):
    raise Exception("Coordenadas fuera de rango.")

S_DISTANCE_TO_ORIGIN = math.dist((0, 0), S)
T_DISTANCE_TO_ORIGIN = math.dist((0, 0), T)

if S_DISTANCE_TO_ORIGIN < T_DISTANCE_TO_ORIGIN:
    STARTING_POINT = S
    ENDING_POINT = T
else:
    STARTING_POINT = T
    ENDING_POINT = S

ST_DISTANCE = math.dist(STARTING_POINT, ENDING_POINT)
DIRECTOR_VECTOR = (
    ENDING_POINT[0] - STARTING_POINT[0],
    ENDING_POINT[1] - STARTING_POINT[1],
)

PRECISION = 3
NORMALIZED_VECTOR = (
    DIRECTOR_VECTOR[0] / (PRECISION * ST_DISTANCE),
    DIRECTOR_VECTOR[1] / (PRECISION * ST_DISTANCE),
)

ESCALARS = set([x for x in range(PRECISION * math.floor(ST_DISTANCE))])
POINT_TO_PAINT = set()

for r in ESCALARS:
    POINT_TO_PAINT.add(
        (
            math.ceil(NORMALIZED_VECTOR[0] * r) + STARTING_POINT[0],
            math.ceil(NORMALIZED_VECTOR[1] * r) + STARTING_POINT[1],
        )
    )

GRID: list = list()
for i in range(RANGO):
    GRID.append(list())
    for j in range(RANGO):
        GRID[i].append("▀")


for CORD in POINT_TO_PAINT:
    GRID[CORD[1]][CORD[0]] = "*"

for i, x in enumerate(reversed(GRID)):
    print(x, len(GRID) - i)

print(sorted(POINT_TO_PAINT))
print(len(POINT_TO_PAINT))
