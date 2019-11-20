def dijkstra(c,n,s):
    d=[0]*n
    vis=[-1]*n
    for i in range(n):
        d[i]=c[s][i]
    d[s]=0
    vis[s]=1
    count,u=1,0
    while count!=n:
        m=999
        for i in range(n):
            if d[i]<m and vis[i]!=1:
                m=d[i]
                u=i
        vis[u]=1
        count+=1
        for  j in range(n):
            if m+c[u][j]<d[j] and vis[j]!=1:
                d[j]=m+c[u][j]

    for i in range(n):
        print(s,"--->",i,":",d[i])
g=[[0,3,2,999,4],
   [3,0,8,999,999],
   [2,8,0,1,999],
   [999,999,1,0,3],
   [4,999,999,3,0]]
dijkstra(g,5,0)    
