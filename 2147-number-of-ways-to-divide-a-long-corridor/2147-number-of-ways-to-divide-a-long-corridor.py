class Solution:
    def numberOfWays(self, corridor: str) -> int:
        m =Counter(corridor)
        if "S" not in m or m["S"] % 2 ==1:
            return 0 
        if m["S"] == 2:
            return 1
        m = defaultdict(int)

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
        return total% MOD
        ans = 1
        for num in m:
            ans *= (num)**m[num] 
        return ans% MOD