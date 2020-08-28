n, m = map(int, input().split())

chart = []

for i in range(n):
    row = list(input())
    chart.append(row)


start_points = []

for i in range(n):
    for j in range(m):
        if chart[i][j] == 'T':
            start_points.append((i,j))


def get_neighbours(graph, coord, n, m):
    x = coord[0]
    y = coord[1]

    neighbours = []
    if x != 0:
        neighbours.append((x-1,y))
    if x != m:
        neighbours.append((x+1,y))
    if y != 0:
        neighbours.append((x, y-1))
    if y != n:
        neighbours.append((x, y+1))

    return neighbours
