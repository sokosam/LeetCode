class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        


        ans = 0
        first = -1
        second = -1
        curr = 0
        lastUsed = -1

        for i in range(len(fruits)):
            if first == -1:
                first = fruits[i]
                lastUsed = i
            elif second == -1 and fruits[i] != first:
                second = fruits[i]
                lastUsed = i
            else:
                if fruits[i] != first and fruits[i] != second:
                    if fruits[lastUsed] == first:
                        second = fruits[i]
                        curr = i - lastUsed  
                        lastUsed = i
                    else:
                        first = fruits[i]
                        curr = i - lastUsed 
                        lastUsed = i
                elif fruits[i] != fruits[lastUsed]:
                    lastUsed = i
            curr +=1
            ans = max(ans,curr)
        return ans
                        