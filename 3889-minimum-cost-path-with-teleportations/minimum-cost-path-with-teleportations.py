import heapq
import math
from typing import List
class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        INF=math.inf
        cells=[]
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j],i,j))
        cells.sort()
        unlocked=[0 for i in range(k+1)]
        distance=[[[INF for i in range(k+1)] for i in range(n)] for i in range(m)]
        distance[0][0][0]=0
        pq=[]
        heapq.heappush(pq,(0,0,0,0))
        while pq:
            cost,i,j,t=heapq.heappop(pq)
            if cost>distance[i][j][t]:
                continue
            if i==m-1 and j==n-1:
                return cost
            for ni,nj in((i,j+1),(i+1,j)):
                if ni<m and nj<n:
                    newcost=cost+grid[ni][nj]
                    if newcost<distance[ni][nj][t]:
                        distance[ni][nj][t]=newcost
                        heapq.heappush(pq,(newcost,ni,nj,t))
            if t<k:
                while unlocked[t]<len(cells) and cells[unlocked[t]][0]<=grid[i][j]:
                    _,x,y=cells[unlocked[t]]
                    unlocked[t]+=1
                    if cost<distance[x][y][t+1]:
                        distance[x][y][t+1]=cost
                        heapq.heappush(pq,(cost,x,y,t+1))
        return min(distance[m-1][n-1])



        