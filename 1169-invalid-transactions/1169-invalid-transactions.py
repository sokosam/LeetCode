class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        

        invalid = set()
        names = defaultdict(list)

        """

        sorted list of name => city/time 
        binseacrh for same city, see if the same city is within 


        """

        for index, tran in enumerate(transactions):
            name, time, amount, city = tran.split(",")
            if int(amount)> 1000:
                invalid.add(tran)
            

            for i in names[name]:
                if abs(int(time) - i[0]) <= 60 and city != i[1]:
                    invalid.add(tran)
                    invalid.add(transactions[i[2]])
                    
            
            names[name].append([int(time), city, index])

        ans = [i for i in transactions if i  in invalid]
        return ans