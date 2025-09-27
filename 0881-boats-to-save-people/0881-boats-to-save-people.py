class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0
        r = len(people) - 1
        total = 0
        while l <=r:
            if l == r:
                return total + 1
            
            if people[r] + people[l] <= limit:
                r -=1
                l +=1
            else:
                r-=1
            total +=1
        return total
