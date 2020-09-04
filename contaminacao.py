from time import sleep

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

def bfs(socketio, graph, start, n, m):
    explored = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            
            if graph[node[0]][node[1]] == 'A':
                graph[node[0]][node[1]] = 'T'
                socketio.emit('update', {'graph': graph})
                sleep(.4)
                
            neighbours = get_neighbours(graph, node, n, m)

            for neighbour in neighbours:
                if get_node(graph, neighbour):
                    queue.append(neighbour)


def start(socketio, graph, n, m):
    start_points = []

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'T':
                start_points.append((i,j))

    for point in start_points:
        bfs(socketio, graph, point, n, m)