class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        

        position.sort()
   
        r  = max(position)
        l = 0


        best = 0


        while l <= r:
            mid = (l + r)//2

            placed = 1
            prev = position[0]
            for i in range(1,len(position)):
                if position[i] - prev < mid:
                    continue
                else:
                    placed +=1
                    prev = position[i]
            
            if placed >= m:
                best = max(mid ,best)
                l = mid + 1
            else:
                r = mid - 1

        return best

                

