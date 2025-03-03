class Solution:
    def frequencySort(self, s: str) -> str:
        

        vals = [[0, chr(x + ord('a')) ] for x in range(26)]
        temp = [[0, chr(x + ord('A')) ] for x in range(26)]
        vals.extend(temp)

        for i in s:
            index = ord(i) - ord('a')
            if index < 0:
                index = ord(i) - ord('A') + 26
            vals[index][0] -= 1

        heapq.heapify(vals)

        ans = ""
        while vals:
            smallest = heapq.heappop(vals)
            amount = -smallest[0]
            letter = smallest[1]

            ans += letter * amount
        return ans

