class Connected_graph:
     def __init__(self,v):
          self.v=v
          self.adj=[[] for i in range(v)]
     def addEdge(self,v,w):
          self.adj[v].append(w)
          self.adj[w].append(v)
     def dfs(self,t,v,visited):
          visited[v]=True
          t.append(v)
          for i in self.adj[v]:
               if visited[i]==False:
                    t=self.dfs(t,i,visited)
          return t
     def connectedcomponents(self):
          visited=[]
          cc=[]
          for i in range(self.v):
               visited.append(False)
          for v in range(self.v):
               if visited[v]==False:
                    t=[]
                    cc.append(self.dfs(t,v,visited))
          return cc

g=Connected_graph(5)
g.addEdge(1,0)
g.addEdge(1,2)
g.addEdge(3,4)
cc=g.connectedcomponents()
print(cc)
