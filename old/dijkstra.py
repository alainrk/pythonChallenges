import heapq

def dijkstra(graph, source, dest):
    q = [(0, source, [])]
    seen = set()

    while True:
        cost, v, path = heapq.heappop(q)
        if v not in seen:
            path = path + [v]
            seen.add(v)
            if v == dest:
                return cost, path
            for (next, c) in graph[v].iteritems():
                if v==6: print next, c
                heapq.heappush(q, (cost + c, next, path))


graph = {
         1:{2:7, 3:9, 6:14},
         2:{1:7, 3:10, 4:15},
         3:{1:9, 2:10, 4:11, 6:2},
         4:{15:2, 3:11, 5:6},
         5:{4:6, 6:9},
         6:{1:14, 3:2, 5:9}
         }

print dijkstra(graph, 1, 5)
