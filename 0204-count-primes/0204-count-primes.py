class Solution:
    def countPrimes(self, n: int) -> int:
        
        primes = [2]

        if n <= 2:
            return 0

        sieve = set([2*i for i in range(1,n - 1)])
        for i in range(2, n):
            if i in sieve:
                continue
    
            primes.append(i)
            for k in range(1, n):
                sieve.add(i*k)
                if i*k >= n:
                    break
        return len(primes)
            