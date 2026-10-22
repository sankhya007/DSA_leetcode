class Solution:
    def canCompleteCircuit(self, gas, cost):

        # initial cost more, cant complete circuit in any way possible
        if sum(gas) < sum(cost):
            return -1

        start = 0
        tank = 0

        # startung from the begenning, if in negetive start from the next step
        for i in range(len(gas)):
            tank += gas[i] - cost[i]

            # if not then increment
            if tank < 0:
                start = i + 1
                tank = 0

        return start