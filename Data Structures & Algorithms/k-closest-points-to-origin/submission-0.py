import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        heapq.heapify(dist)
        map_dist = {}
        for i in points:
            rad = i[0]*i[0] + i[1]*i[1]
            heapq.heappush(dist,rad)
            if map_dist.get(rad):
                map_dist[rad].append(i)
            else:
                map_dist[rad] = [i]
        out = []
        for _ in range(k):
            key = heapq.heappop(dist)
            out.append(map_dist[key].pop())
        return out

                    

