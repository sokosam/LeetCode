class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:

        lights = [[light[0] + light[1], light[0] - light[1]] for light in lights]
        lights.sort(key = lambda x : x[1])
        heap = []
        best = 0
        bestIndex = None
        for light in lights:
            leftEdge = light[1] 
            rightEdge = light[0] 

            while len(heap) > 0 and leftEdge > heap[0][0] :
                heapq.heappop(heap)

            heapq.heappush(heap, [rightEdge, leftEdge])
            if len(heap) > best:
                best = len(heap)
                bestIndex = leftEdge

        return bestIndex
            

            