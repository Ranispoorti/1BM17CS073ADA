global visited,n,m,vertex_queue
n = int(input())
m = int(input())
visited = [[None]*m for i in range(n)]
vertex_queue = []

class Queue:
   def __init__(self,row,col,dist):
     self.row = row
     self.col = col
     self.dist = dist
def minDist(graph):
  source = Queue(0,0,0)
  for i in range(n):
    for j in range(m):
      if graph[i][j] == '0':
         visited[i][j] = True
      else:
         visited[i][j] = False
      if graph[i][j] == 's':
         source.row = i
         source.col = j
         vertex_queue.append(source)
         visited[source.row][source.col] = True
  while len(vertex_queue) != 0:
    item = vertex_queue.pop(0)
    if graph[item.row][item.col] == 'd':
       return item.dist
    if item.row - 1 >= 0 and visited[item.row - 1][item.col] == False:
       vertex_queue.append(Queue(item.row-1, item.col, item.dist+1))
       visited[item.row-1][item.col] = True
    if item.row + 1 < n and visited[item.row + 1][item.col] == False:
       vertex_queue.append(Queue(item.row+1, item.col, item.dist+1))
       visited[item.row+1][item.col] = True
    if item.col - 1 >= 0 and visited[item.row][item.col-1] == False:
       vertex_queue.append(Queue(item.row, item.col-1, item.dist+1))
       visited[item.row][item.col-1] = True
    if item.col + 1 < m and visited[item.row][item.col + 1] == False:
       vertex_queue.append(Queue(item.row, item.col+1, item.dist+1))
       visited[item.row][item.col+1] = True
    return -1

graph=[]
for i in range(n):
 graph.append(input().split())
print(minDist(graph))
