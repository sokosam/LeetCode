class Solution:
    def numOfSubsequences(self, s: str) -> int:
        """



        LLTL C LTLTT

        # new LCT's formed = (#L on the left)  * (#T on the right)

        lets have a prefix sum of all L, C , and T

        LCCT
                     x   
        prefixL = [1,1,1,1]
        prefixC = [0,1,2,2]
        prefixT = [0,0,0,1]

        If im a C:
            I need know how many Ls are before me, and how many Ts are ahead of me.
            So to do this, we can take L = prefixL[x - 1]
            and the T = prefixT[-1] - prefixT[x]
            and so we can do T*L to find how many LCT's

        To determine the best place to place an C:
            we want to find the position where T*L is greatest

        For L we would place it at the front and basically get C*T as how many subsequences we will get

        for T we place it at the end, L*C 

        """

        prefixL = [0]
        prefixC = [0]
        prefixT = [0]

        for index,i in enumerate(s):
            if i == "L":
                prefixL.append( 1 + prefixL[index])
                prefixC.append(prefixC[index])
                prefixT.append(prefixT[index])
            elif i == "C":
                prefixL.append(  prefixL[index])
                prefixC.append(1 + prefixC[index])
                prefixT.append(prefixT[index])
            elif i == "T":
                prefixL.append(  prefixL[index])
                prefixC.append(prefixC[index])
                prefixT.append( 1 +prefixT[index])
            else:
                prefixL.append( prefixL[index])
                prefixC.append(prefixC[index])
                prefixT.append(prefixT[index])

        totalLCTs = 0

        for i in range(1, len(prefixC)):
            if prefixC[i -1] != prefixC[i]:
                totalLCTs += prefixL[i]*(prefixT[-1] - prefixT[i])


        bestCPlace = [0]
        for i in range(1,len(prefixL)):
            bestCPlace.append(prefixL[i]* (prefixT[-1] - prefixT[i]))

        bestC = max(bestCPlace)
        bestL = 0
        for i in range(1, len(prefixT)):
            if prefixT[i - 1] != prefixT[i]:
                bestL += prefixC[i]

        bestT = 0

        for i in range(len(prefixT) -1, 0 , -1):
            if prefixL[i - 1] != prefixL[i]:
                bestT += prefixC[-1] - prefixC[i]
        print(bestL,bestC,bestT)
        return totalLCTs + max(bestC,bestL,bestT)
        
