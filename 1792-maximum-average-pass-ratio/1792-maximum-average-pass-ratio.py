class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        
        filled = [1 for i in classes if i[0] == i[1]]
        classes = [ [ -((c[0] +1)/(1 + c[1]) - c[0]/c[1]) , c[0], c[1] ] for c in classes if c[0] != c[1]]
        heapq.heapify(classes)

        while len(classes) > 0 and extraStudents > 0:
            curr = heapq.heappop(classes)
            newTotal = curr[2] + 1
            newPassed = curr[1] + 1
            newPotential = -((newPassed + 1)/(newTotal + 1) - (newPassed)/newTotal)
            heapq.heappush(classes, [newPotential, newPassed, newTotal])
            extraStudents-=1

        
        ans = 0

        for i in classes:
            ans += i[1]/i[2]
        return (ans + 1*len(filled) )/(len(classes) + len(filled))
