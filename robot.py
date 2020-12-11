#Cracking the coding interview question 8.2
#Space Complexity : O(N*M)
#Time Complexity : O(2**N)
def robotGrid(i,j,grid,path,failed,N,M):
    #Maitaining an array of failed points
    if  i>=N or j>=M or failed[i][j]==True:
        return False
    elif grid[i][j]==1 :
        failed[i][j]=True
        return False
    path.append((i,j))
    if i==(N-1) and j==(M-1):
        return True
    if robotGrid(i,j+1,grid,path,failed,N,M) or robotGrid(i+1,j,grid,path,failed,N,M):
        return True
    else:
        #for a point at which both the right and bottom neighbours are unfit for move,
        #the point becomes a failed point
        failed[i][j]=True
        path.pop()
        return False

grid=[[0,0,0,0,1],
      [0,0,1,1,0],
      [0,0,0,0,0]]
N=len(grid)
M=len(grid[0])
failed = [[False] * M for i in range(N)]
path=[]

if robotGrid(0,0,grid,path,failed,3,5):
    print(path)
else:
    print("Path does not exist")