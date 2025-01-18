class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7  # Define the modulo value
        countPrime = n // 2
        countEven = n - countPrime

        def binaryExponentiation(base, exp, mod):
            res = 1
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % mod  # Take modulo during multiplication
                base = (base * base) % mod  # Take modulo during squaring
                exp //= 2
            return res

        # Calculate the result with modulo
        result = (binaryExponentiation(5, countEven, MOD) * binaryExponentiation(4, countPrime, MOD)) % MOD
        return result
