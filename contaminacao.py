def get_neighbours(graph, coord, n, m):
    x = coord[0]
    y = coord[1]

    neighbours = []
    if x != 0:
        neighbours.append((x-1,y))
    if x != n-1:
        neighbours.append((x+1,y))
    if y != 0:
        neighbours.append((x, y-1))
    if y != m-1:
        neighbours.append((x, y+1))

    return neighbours

def get_node(graph, coord):
    return graph[coord[0]][coord[1]] == 'T' or graph[coord[0]][coord[1]] == 'A'

def bfs(graph, start, n, m):
    explored = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            neighbours = get_neighbours(graph, node, n, m)

            for neighbour in neighbours:
                if get_node(graph, neighbour):
                    queue.append(neighbour)
    return explored

def change_node(chart, initial_node, n, m):
    explored = bfs(chart, initial_node, n, m)
    for node in explored:
        if chart[node[0]][node[1]] == 'A':
            chart[node[0]][node[1]] = 'T'


n, m = map(int, input().split())

while n != 0:
    chart = []

    for i in range(n):
        row = list(input())
        chart.append(row)


    start_points = []

    for i in range(n):
        for j in range(m):
            if chart[i][j] == 'T':
                start_points.append((i,j))

    for point in start_points:
        change_node(chart, point, n, m)

    for i in range(n):
        for j in range(m):
            print(chart[i][j], end='')
        print()
    
    print()
    n, m = map(int, input().split())
