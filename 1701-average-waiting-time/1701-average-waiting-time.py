class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        time = customers[0][0]
        total = 0
        for customer in customers:
            if time > customer[0]:
                total += time - customer[0] + customer[1]
            else:
                total += customer[1]
            time = max(time, customer[0]) + customer[1]
        return total/len(customers)