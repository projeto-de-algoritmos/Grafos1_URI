n = int(input())
start, goal = map(str, input().split())

graph = {}
paths = []

def create_edge(node, graph, word):
  if graph.get(node):
    graph[node]['array'].append(word)
  else:
    graph[node] = {'array': [word], 'type': 'language'}
  
  graph[node]['type'] = 'language'

  if graph.get(word):
    graph[word]['array'].append(node)
  else:
    graph[word] = {'array': [node], 'type': 'word'}

  graph[word]['type'] = 'word'

def dfs_all_paths(graph,start,goal,path=[]): 
  path=path+[start] 
  if start==goal:
    paths.append(path) 
    print(path)
  for neighbour in graph[start]['array']:
    if neighbour not in path:
      dfs_all_paths(graph,neighbour,goal,path)

for i in range(n):
  node1, node2, word = map(str, input().split())
  create_edge(node1, graph, word)
  create_edge(node2, graph, word)

dfs_all_paths(graph, start, goal)



    
