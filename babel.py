def create_edge(node, graph, word):
  if graph.get(node):
    graph[node]['array'].append({'value': word, 'type': 'word'})
  else:
    graph[node] = {'array': [{'value': word, 'type': 'word'}], 'type': 'language'}

  graph[node]['type'] = 'language'

  if graph.get(word):
    graph[word]['array'].append({'value': node, 'type': 'language'})
  else:
    graph[word] = {'array': [{'value': node, 'type': 'language'}], 'type': 'word'}

  graph[word]['type'] = 'word'

def dfs_all_paths(graph,start,goal,path=[]):
  path=path+[start]
  if start['value']==goal['value']:
    paths.append(path)
  for neighbour in graph[start['value']]['array']:
    if neighbour not in path:
      dfs_all_paths(graph,neighbour,goal,path)


n = int(input())

while n != 0:
  start, goal = map(str, input().split())

  graph = {}
  paths = []
  lengths = []


  for i in range(n):
    node1, node2, word = map(str, input().split())
    create_edge(node1, graph, word)
    create_edge(node2, graph, word)


  dfs_all_paths(graph, {'value': start, 'type': 'language'}, {'value': goal, 'type': 'language'})



  if not paths:
    print('impossivel')
  else:
    for path in paths:
      words = [node['value'] for node in path if node['type'] == 'word']
      length = 0
      valid_path = True

      for i in range(len(words)):
        if i != 0:
          if words[i][0] == words[i - 1][0]:
            valid_path = False
            break
        length += len(words[i])
      
      if valid_path:
        lengths.append(length)


    print(min(lengths))

  n = int(input())
