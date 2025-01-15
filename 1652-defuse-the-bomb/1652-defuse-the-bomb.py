class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: return [0] * len(code)

        ans = []
        if k > 0:
            window = 0
            for i in range(k):
                window += code[i]
            k-=1
            for i in range(len(code)):
                window -= code[i]
                k += 1
                if k >=len(code):
                    k = 0
                window += code[k]
                ans.append(window)
        else:
            window = 0
            for i in range(k - 1 , -1):
                window += code[i]
            for i in range(len(code)):
                window += code[i - 1]
                window -= code[k -1]
                k+= 1
                ans.append(window)
            
        return ans