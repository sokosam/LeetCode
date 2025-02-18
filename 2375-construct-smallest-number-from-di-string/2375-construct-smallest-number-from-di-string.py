class Solution:
    def smallestNumber(self, pattern: str) -> str:
        

        s = ""
        p = []

        for i in range(len(pattern)):

            p.append(str(i + 1))

            if pattern[i] == "I":
                while p:
                    s += p.pop()
        
        p.append(str(len(pattern) + 1))
        while p:
            s += p.pop()
        return s