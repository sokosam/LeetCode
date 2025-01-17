class Solution:
    def findComplement(self, num: int) -> int:
        n = 0
        while 2**n <= num:
            n+=1

        return ~ num + 2**n