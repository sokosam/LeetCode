class Solution:
    def minimumSteps(self, s: str) -> int:
        x = []
        for i in s:
            x.append(i)
        print(x)

        while x[-1] == "1":
            x.pop()
        
        swaps = 0
        consec = 0
        size = len(x)
        r = size
        for i in range(size):
            if x[i] == "1":
                swaps += r - i - 1
                r -= 1
            # else:

        return swaps
                