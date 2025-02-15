class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        S = [0]
        for i in range(n - 1):

            new = [1]* (2*len(S) + 1)

            for i in range(len(S)):
                new[i] = S[i]
                new[-i - 1] = S[i] ^ 1
            new[len(new)//2] = 1
            S = new
        # print(S)
        return str(S[k - 1])