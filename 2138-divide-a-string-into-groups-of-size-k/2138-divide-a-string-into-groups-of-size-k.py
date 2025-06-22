class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        newStr = [s[k*i:k*(i+1)] for i in range(len(s)//k)]
        if len(newStr)*k < len(s):
            new = s[k*(len(s)//k - 1) +k:]
            new += fill*(k - len(new))
            newStr.append(new)
        return newStr