class Solution:
    def numberOfWays(self, corridor: str) -> int:

        ptr = 0
        chair_count = 0
        last_seen = 0
        total = 1
        MOD = 10**9 + 7

        while ptr < len(corridor):
            if corridor[ptr] == "S":
                chair_count += 1
                if chair_count > 2 and chair_count % 2 == 1:
                    total*= (ptr - last_seen) % MOD
                last_seen = ptr
            ptr +=1
        if chair_count < 2 or chair_count % 2 == 1:
            return 0
        return total% MOD
