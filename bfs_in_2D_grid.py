from queue import Queue
def isValid(x,y,N,M):
    if x>=N or x<0 or y<0 or y>=M:
        return False
    return True
def bfs(grid,queue,N,M):
    directions=[[1,0],[0,1],[-1,0],[0,-1]]
    while not queue.empty():
        current=queue.get()
        x,y=current[0],current[1]
        if visited[x][y]!=True:
            visited[x][y]=True
            print("Visited="+str(grid[x][y]))
            for dir in directions:
                if isValid(x+dir[0],y+dir[1],N,M):
                    queue.put((x+dir[0],y+dir[1]))

grid=[[1,2,3],
      [4,5,6],
      [7,8,9]]
q=Queue()
q.put((0,0))
N=len(grid)
M=len(grid[0])
visited=[[False]*M for i in range(N)]
bfs(grid,q,N,M)