class Solution:
    def countCollisions(self, directions: str) -> int:
        s = [ ]
        crashes = 0
        for i in directions:
            if i == "S":
                while len(s) > 0 and s[-1] == "R":
                    s.pop()
                    crashes +=1
                s.append("S")
            elif i == "L":
                if len(s) > 0:
                    crashes +=1
                    while s and s[-1] == "R":
                        s.pop()
                        crashes +=1
                        if len(s) == 0:
                            s.append("S")
            else:
                s.append("R")

        return crashes