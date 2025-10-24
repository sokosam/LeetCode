class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        k = n + 1
        while True:
            nums = [int(i) for i in str(k)]
            c = Counter(nums)
            fails = False
            for i in c:
                if c[i] != i:
                    fails = True
            if not fails:
                return k
            else:
                k +=1

            

                
                
