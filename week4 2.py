class Graph: 
    def __init__(self, row, col, g): 
        self.r = row 
        self.c = col 
        self.graph = g 
    def isSafe(self, i, j, visited): 
        return (i >= 0 and i < self.r and 
                j >= 0 and j < self.c and 
                not visited[i][j] and self.graph[i][j]) 
    def DFS(self, i, j, visited): 
        ro = [-1, -1, -1,  0, 0,  1, 1, 1]; 
        co = [-1,  0,  1, -1, 1, -1, 0, 1]; 
        visited[i][j] = True
        for k in range(8): 
            if self.isSafe(i + ro[k], j + co[k], visited): 
                self.DFS(i + ro[k], j + co[k], visited) 
    def countIslands(self): 
        visited = [[False for j in range(self.c)]for i in range(self.r)] 
        count = 0
        for i in range(self.r): 
            for j in range(self.c): 
                if visited[i][j] == False and self.graph[i][j] == 1: 
                    self.DFS(i, j, visited) 
                    count += 1
        return count 
graph = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 1]] 
row = len(graph) 
col = len(graph[0])  
g = Graph(row, col, graph) 
print(g.countIslands()) 
