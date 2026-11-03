class Solution:
    def longestDupSubstring(self, s: str) -> str:
        
        # def check(string, l):
        #     seen = set()
        #     curr = []
        #     for end in range(len(string)):
        #         curr.append(string[end])
        #         if len(curr) > l:
        #             curr.pop(0)
        #         if len(curr) == l:
        #             key = tuple(curr)
        #             if key in seen:
        #                 return curr
        #             seen.add(key)
        #     return []

        def check(string, l):
            n = len(string)
            if l > n:
                return ""
            base = 26
            mod = (1 << 61) - 1
            power = pow(base, l, mod)  # base^l, used to drop the leftmost char

            h = 0
            seen = {}  # hash -> list of start indices with that hash
            for end in range(n):
                # add the new char on the right
                h = (h * base + ord(string[end]) - 97) % mod
                # once the window is longer than l, drop the char on the left
                if end >= l:
                    h = (h - (ord(string[end - l]) - 97) * power) % mod
                if end >= l - 1:
                    start = end - l + 1
                    sub = string[start:end + 1]
                    if h in seen:
                        # compare actual strings to rule out a hash collision
                        for j in seen[h]:
                            if string[j:j + l] == sub:
                                return sub
                        seen[h].append(start)
                    else:
                        seen[h] = [start]
            return ""

        l = 1
        r = len(s)
        best = ""
        while l <=r:
            m = l + (r-l)//2

            x = check(s,m)
            # print(x)
            if len(x) > 0:
                best = "".join(x)
                l = m + 1
            else:
                r = m -1
        return best