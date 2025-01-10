class Solution:
    def fib(self, n: int) -> int:
        prev = 0
        curr = 1

        if n == 0: return 0

        itr = 1

        while itr < n:
            prev, curr = curr, prev + curr
            itr += 1
        
        return curr
