class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        x = 0
        for i in range(1,n + 1):
            if i % m == 0:
                x+= i
        return (n*(n+1))//2 - 2*x