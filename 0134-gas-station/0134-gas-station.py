class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """

        [3, 7, 12, 13, 15]
        [2,  4]

        """

        stuck = -1

        station = 0
        while station < len(gas):
            temp = station

            currGas = gas[station]

            nextStation = cost[(temp) % len(gas)]
            if currGas < nextStation:
                station +=1
                continue
            else:
                currGas -= cost[temp]
                temp = (temp +1)%len(gas)
                currGas += gas[temp]
                while currGas >= cost[temp] and temp != station:
                    currGas -= cost[temp]
                    temp = (temp +1)%len(gas)
                    currGas +=gas[temp]
                
                if temp == station:
                    return station
                else:
                    if temp < station:
                        return -1
                    else:
                        station = temp
        return -1
