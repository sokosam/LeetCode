class Solution:
    def candy(self, ratings: List[int]) -> int:
        """


            1 0 2

            1 1 1


            2 1 2


            x x x x x x x min x x x max x x x min


        """

        test = [-1]* len(ratings)
        if len(ratings) == 1:
            return 1

        def getVal(index):
            nonlocal test
            if test[index] != -1:
                return test[index]
            
            if index < 0 or index >= len(test):
                return 0
            
            if index == 0:
                if ratings[index + 1] < ratings[index]:
                    test[index] = getVal(index + 1)  + 1
                else:
                    test[index] = 1
                return test[index]
            if index == len(ratings) - 1:
                if ratings[index - 1] < ratings[index]:
                    test[index] = getVal(index - 1)  + 1
                else:
                    test[index] = 1
                return test[index]

            if ratings[index -1 ] >= ratings[index] and ratings[index +1] >= ratings[index]:
                test[index] = 1
                return 1
            elif ratings[index - 1] < ratings[index] and ratings[index + 1] < ratings[index]:
                test[index] = max(getVal(index -1) +1, getVal(index + 1) + 1)
                return test[index]
            elif ratings[index - 1] < ratings[index]:
                test[index] = getVal(index - 1)  + 1
                return test[index]
            else:
                test[index] = getVal(index + 1) + 1
                return test[index]
        
        for i in range(len(ratings)):
            getVal(i)
        print(test)
        return sum(test)