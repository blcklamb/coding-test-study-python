import heapq
import sys
input = sys.stdin.readline
cityNum = int(input())
busNum = int(input())
busInfo ={List1: {} for List1 in range(cityNum+1)}
# {0: {}, 1: {2: 2, 3: 3, 4: 1, 5: 10}, 2: {4: 2}, 3: {4: 1, 5: 1}, 4: {5: 3}, 5: {}}
distance = [float('inf')]*(cityNum+1)
visited = [False]*(cityNum+1)

for _ in range(busNum):
    start, end, cost = map(int, input().split())
    
    if end in busInfo[start].keys():
        busInfo[start][end] = min(busInfo[start][end], cost)
    else:
        busInfo[start][end] = cost
    '''
    2
    2
    1  2  10
    1  2  20
    // 10
    // 20
    busInfo[start][end] = cost
    '''

startCity, endCity = map(int, input().split())

def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    queue = []
    heapq.heappush(queue, (distance[start], start))

    while queue:
        curDistance, curNode = heapq.heappop(queue)
        if distance[curNode] < curDistance:
            continue 
        for adjacent, weight in busInfo[curNode].items():
            distanceNow = curDistance + weight
            if distanceNow < distance[adjacent]:
                distance[adjacent] = distanceNow
                heapq.heappush(queue, (distanceNow, adjacent))

dijkstra(startCity)

print(distance[endCity])