class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        twoes = []
        curr = 1

        while curr <= 10**9:
            new = [0]*10
            strCurr = str(curr)
            for i in strCurr:
                new[int(i)] += 1
            curr *=2
            twoes.append(new)

        digits = [0]*10
        for i in str(n):
            digits[int(i)] +=1

        for two in twoes:
            correct = True
            for i in range(len(two)):
                if two[i] != digits[i]:
                    correct = False
            if correct:
                return True
        print(twoes)
        print(digits)
        return False

