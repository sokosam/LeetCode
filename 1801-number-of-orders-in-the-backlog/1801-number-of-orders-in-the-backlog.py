class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []

        for order in orders:
            # print(buy,sell)
            price, amount, orderType = order

            if orderType == 1:
                while buy and -buy[0][0] >= price and amount > 0:
                    buy_price, buy_amount = heapq.heappop(buy)

                    if amount >= buy_amount:
                        amount -= buy_amount
                    else:
                        buy_amount -= amount
                        amount = 0
                        if buy_amount > 0:
                            heapq.heappush(buy, [buy_price, buy_amount])
                if amount > 0:
                    heapq.heappush(sell, [price, amount])
            else:
                while sell and sell[0][0] <= price and amount > 0:
                    sell_price, sell_amount = heapq.heappop(sell)
                    # print(amount, sell, price, sell_price, sell_amount)
                    if amount >= sell_amount:
                        amount -= sell_amount
                    else:
                        sell_amount -= amount
                        amount = 0
                        if sell_amount > 0:
                            heapq.heappush(sell, [sell_price, sell_amount])
                if amount > 0:
                    heapq.heappush(buy, [-price, amount])
        
        print(buy, sell)
        MOD = 10**9 + 7
        total = 0
        for i in buy:
            total += i[1] % MOD
        for i in sell:
            total += i[1] % MOD
 
        return total % MOD
                    