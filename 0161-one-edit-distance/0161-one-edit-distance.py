class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        if abs(len(s) - len(t)) >1:
            return False
        if len(s) == len(t):
            ptr = 0
            foundOne = False
            while ptr < len(s):
                if s[ptr] != t[ptr]:
                    if foundOne:
                        return False
                    else:
                        foundOne = True
                ptr +=1
            return True
        larger = t
        smaller = s
        if len(s) > len(t):
            larger = s
            smaller = t
        
        ptr = 0

        while ptr < len(smaller):
            if larger[ptr] != smaller[ptr]:
                return larger[ptr +1:] == smaller[ptr:] or larger[ptr:] == smaller[ptr +1:]
            ptr +=1
        return True
        