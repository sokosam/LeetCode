class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        cols_per_row = len(encodedText)//rows


        s = []

        for i in range(0, cols_per_row):
            curr =i
            while curr < len(encodedText):
                s.append(encodedText[curr])
                curr += cols_per_row + 1
        
        while s and s[-1] == " ":
            s.pop()
        return "".join(s)