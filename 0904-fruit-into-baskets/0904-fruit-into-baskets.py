class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        numDistinct = 0

        count = defaultdict(int)

        ans ,start =0,0

        for end in range(len(fruits)):
            count[fruits[end]] +=1

            if count[fruits[end]] == 1:
                numDistinct +=1
            
            while numDistinct >2:
                count[fruits[start]] -=1
                if count[fruits[start]] == 0:
                    numDistinct -=1
                start +=1
            
            ans = max(ans, end - start + 1)

        return ans