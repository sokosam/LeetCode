class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        
        
        transactions_cb_less = [i for i in transactions if i[0] > i[1] ]
        # transactions_cb_less_zero = [i for i in transactions if i[0] > i[1] and i[1] == 0]

        transactions_cb_equal = [ i for i in transactions if i[0] == i[1]]
        transactions_cb_greater = [i for i in transactions if i[1] > i[0]]

        transactions_cb_ge = transactions_cb_equal + transactions_cb_greater
        transactions_cb_ge.sort(reverse = True, key = lambda x : x[0])

        transactions_cb_less.sort(key = lambda x : x[1])
        # print(transactions_cb_ge)
        # print(transactions_cb_less)

        leftover = 0
        start = 0
        curr = 0


        for i in transactions_cb_less:
            if curr < i[0]:
                start += i[0] - curr
                curr = i[1]
            else:
                curr -= i[0]
                curr += i[1]
        print(transactions_cb_less)
        print(start)
        print(transactions_cb_ge)
        
        # start = start + sum([ i[0] for i in transactions_cb_less ])
        if len(transactions_cb_ge) == 0:
            worst = 0
        else:
            worst = max([i[0] for i in transactions_cb_ge])
            if curr > worst:
                start = max(start, worst)
            else:
                start -= curr
                start = start + worst 
        return start
