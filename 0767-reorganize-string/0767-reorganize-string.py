class Solution:
    def reorganizeString(self, s: str) -> str:
        
        items = {}
        for i in s:
            if i not in items:
                items[i] = 1
            else:
                items[i] +=1

        pq = [(-items[i], i) for i in items]

        heapq.heapify(pq)
        prev = ""
        ans = []
        while pq:

            if pq[0][1] == prev:
                val = heapq.heappop(pq)
                if len(pq) == 0:
                    return ""
                val2 = heapq.heappop(pq)
                ans.append(val2[1])
                if val2[0] + 1 != 0:
                    heapq.heappush(pq,(val2[0] +1, val2[1]))
                heapq.heappush(pq ,val)
                prev = val2[1]
            else:
                val = heapq.heappop(pq)
                ans.append(val[1])
                if val[0] + 1 != 0:
                    heapq.heappush(pq,(val[0] + 1, val[1]))
                prev = val[1]
        return "".join(ans)