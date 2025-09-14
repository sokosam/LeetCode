class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas < total cost, impossible.
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                # Can't reach i+1 from current start; next start is i+1
                start = i + 1
                tank = 0
        return start
