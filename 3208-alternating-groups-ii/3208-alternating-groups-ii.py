class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        

        prev = -1
        count = 0
        ans = 0
        """

        1 2 3 4 5
        1 2 3 
          2 3 4
            3 4 5

        1 2 3 4
        1 2 3
          2 3 4
        
        1 2 3 4 5 6 
        1 2 3
          2 3 4
            3 4 5
              4 5 6

        """
        
        circle = -1
        start = -1
        for i in colors:
            if prev == -1:
                start = i
                prev = i
                count = 1
            elif prev == i:
                ans += max(0, count - k + 1)
                if circle == -1:
                    circle =count
                count = 1
            else:
                prev = i
                count += 1
            print(count)
        if start == colors[-1]:
            circle = 0
        if circle < 0:
            return len(colors)

        print(circle)
        ans += max(0, circle + count - k + 1)
        return ans

