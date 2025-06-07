class Solution:
    def clearStars(self, s: str) -> str:

        count = [[] for _ in range(26)]
        h = []
        for i in range(len(s)):
            if s[i] != "*":
                value = s[i]
                ordVal = ord(value) - ord('a')
                count[ordVal].append(i)
                if len(count[ordVal]) == 1:
                    heapq.heappush(h, value)
            else:
                small = heapq.heappop(h)
                smallest = ord(small) - ord("a")
                count[smallest].pop()
                if len(count[smallest]) != 0:
                    heapq.heappush(h, small)
        ans = ["*"]*len(s)


        for i in range(len(count)):
            for k in count[i]:
                ans[k] = chr(i + ord('a'))

        z = ""

        for i in ans:
            if i != "*":
                z += i
        return z
            
        # c = {}
        # for i in range(len(s)):
        #     if s[i] not in c:
        #         c[s[i]] = [i]
        #     else:
        #         c[s[i]].append(i)
        
        # heap = [[i, c[i]] for i in c if i != "*"]
        # heapq.heapify(heap)
        
        # if "*" not in c:
        #     return s
        # amt = len(c["*"])

        # while amt > 0:
        #     item = heapq.heappop(heap)

        #     item[1].pop()
        #     if len(item[1]) != 0:
        #         heapq.heappush(heap,item)
        #     amt -=1
        
        # ans = ["*"]*len(s)

        # while heap:
        #     item = heapq.heappop(heap)
        #     for i in item[1]:
        #         ans[i] = item[0]
        
        # s = ""
        # for i in ans:
        #     if i != "*":
        #         s += i
        # return s
            