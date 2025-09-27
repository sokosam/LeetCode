class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        

        """

        XDir = [-1,-1,-2]

        -2 +1 = -1
        1 - 0 = 1


        YDir = [0,1,1]


        """

        preX = [0]
        preY = [0]


        for i in s:
            dx= 0
            dy =0
            if i == "L":
                dx = -1
            elif i == "R":
                dx = 1
            elif i == "U":
                dy = 1
            elif i == "D":
                dy = -1
            preX.append(preX[-1] + dx)
            preY.append(preY[-1] + dy)
        
        preX.append(preX[-1])
        preY.append(preY[-1])
        # print(preX,preY)
        start = 1
        combos = set()
        for end in range(1, len(preX) - 1):
            if end - start + 1 == k:
                finalx = preX[-1] - preX[end] + preX[start - 1]
                finaly = preY[-1] - preY[end] + preY[start - 1]
                combos.add((finalx,finaly))
                start +=1
            end += 1
        # print(combos)
        return len(combos)


            