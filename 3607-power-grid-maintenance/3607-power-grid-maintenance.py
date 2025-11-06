class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        """

        [X] - [2]
         |     |
        [3] - [4]

        lowest number of x => heap

        [1,2,3,4]

        instead removing from the heap immedieatly we can instead check until we find the first online station

        pop(1)
        [2,3,4]



        """

        parent = [i for i in range(1, c + 1)]

        for connection in connections:
            left, right = connection[0], connection[1]

            # Find root of left with path compression
            orig_left = left
            while parent[left - 1] != left:
                parent[left - 1] = parent[parent[left - 1] - 1]
                left = parent[left - 1]
            
            # Find root of right with path compression
            orig_right = right
            while parent[right - 1] != right:
                parent[right - 1] = parent[parent[right - 1] - 1]
                right = parent[right - 1]
            
            # Now 'left' and 'right' are roots
            if left != right:
                if left < right:
                    parent[right - 1] = left
                else:
                    parent[left - 1] = right

        # Final path compression for all nodes
        online = [True] * c
        for index in range(c):
            curr = index + 1
            while parent[curr - 1] != curr:
                parent[curr - 1] = parent[parent[curr - 1] - 1]
                curr = parent[curr - 1]
            parent[index] = curr
        print(parent)
        stationMap = {}
        grid = defaultdict(list)

        for index,station in enumerate(parent):
            stationMap[index + 1] = station
            heappush(grid[station], index + 1)
        ans = []
        for query in queries:
            if query[0] == 1:
                if online[query[1] -1]:
                    ans.append(query[1])
                    continue
                current_grid = stationMap[query[1]]
                heap = grid[current_grid]
                
                while heap:
                    if not online[heap[0]-1]:
                        heapq.heappop(heap)
                    else:
                        ans.append(heap[0])
                        break
                if len(heap) == 0:
                    ans.append(-1)
            else:
                online[query[1] - 1] = False 
        return ans
