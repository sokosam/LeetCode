class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        freq = Counter(s)
        m = max(freq.values())

        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact = [1] * (m + 1)
        inv_fact[m] = pow(fact[m], MOD - 2, MOD)
        for i in range(m, 0, -1):
            inv_fact[i - 1] = inv_fact[i] * i % MOD

        def choose(n, k):
            if k > n:
                return 0
            return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

        good = 0
        for k in range(1, m + 1):
            good_at_k = 1
            for times in freq.values():
                good_at_k = good_at_k * (1 + choose(times, k)) % MOD
            good = (good + good_at_k - 1) % MOD
        return good



