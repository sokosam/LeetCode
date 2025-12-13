class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        ans = []
        m = defaultdict(list)
        for entry in range(len(code)):
            if not isActive[entry]:
                continue
            if businessLine[entry] not in {"electronics", "grocery", "pharmacy", "restaurant"}:
                continue
            if len(code[entry]) == 0:
                continue

            valid = True
            for char in code[entry]:
                if not char.isalnum() and char != "_":
                    valid = False
            
            if valid:
                m[businessLine[entry]].append(code[entry])
        return m["electronics"] + m["grocery"] + m["pharmacy"] + m["restaurant"]



