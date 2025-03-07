class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
            def SieveOfEratosthenes(left, n):
                prime = [True for i in range(n+1)]
                p = 2
                while (p * p <= n):
                    if (prime[p] == True):

                        for i in range(p * p, n+1, p):
                            prime[i] = False
                    p += 1
                best = [-1,-1]
                prev = -1
                for p in range(left, n+1):
                    if prime[p]:
                        if prev >= 2 and ((best[1] - best[0] > p - prev) or best[1] == -1):
                            best[1] = p
                            best[0] = prev
                        prev = p
                return best

            return SieveOfEratosthenes(left, right)
                            

            