class Solution:
    def frequencySort(self, s: str) -> str:
        

        vals = [[0, chr(x + ord('a')) ] for x in range(26)]
        upper = [[0, chr(x + ord('A')) ] for x in range(26)]
        digits = [[0 , str(x)] for x in range(10)]
        vals.extend(upper)
        vals.extend(digits)

        for i in s:
            index = 0
            if i.isnumeric():
                index = 52 + int(i)
            elif  ord(i) - ord('a') < 0:
                index = ord(i) - ord('A') + 26
            else:
                index = ord(i) - ord('a')
            vals[index][0] -= 1

        heapq.heapify(vals)

        ans = ""
        while vals:
            smallest = heapq.heappop(vals)
            amount = -smallest[0]
            letter = smallest[1]

            ans += letter * amount
        return ans

