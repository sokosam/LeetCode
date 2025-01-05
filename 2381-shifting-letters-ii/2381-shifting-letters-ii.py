class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        # d z t z
        # 0 0 0 0
        #-1 2 0 0
        # c a t z
        sh = [0]*(len(s) + 1)
        change = 0
        for i in shifts:
            change = -1 if i[2] == 0 else 1
            sh[i[0]] += change
            sh[i[1] + 1] -= change
        print(sh)
        result = list(s)
        curr = 0
        for i in range(len(s)):
            letter = ord(s[i]) - ord('a')
            curr += sh[i]
            letter += curr
            letter %= 26


            
            result[i] = chr(letter + ord('a'))
        return "".join(result)



                
