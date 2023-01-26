class Solution:
    # O((|e| + |v|) * log|v|) time and O(|v| + |e|) space
    def dijkstra(self, graph, src, dst, k):
        prices: DefaultDict[int, int] = defaultdict(lambda: float("inf"), {src: 0})
        stops: DefaultDict[int, Optional[int]] = defaultdict(lambda: 0)
        priortyQueue = [(0, src, k + 1)]
        
        while priortyQueue:
            price, city, steps = heapq.heappop(priortyQueue)

            if city == dst:
                return price
            
            if stops[city] >= steps:
                continue
            
            stops[city] = steps
            for neighbor, cost in graph[city].items():
                heapq.heappush(priortyQueue, (price + cost, neighbor, steps - 1))
        
        return -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph: DefaultDict[int, DefaultDict[int, int]] = defaultdict(lambda: {})
        for flight in flights:
            source, destination, cost = flight
            graph[source][destination] = cost
        
        return self.dijkstra(graph, src, dst, k)
