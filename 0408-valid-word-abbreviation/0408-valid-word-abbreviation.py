class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        ptr = 0

        i = 0
        while i < len(abbr):
            if abbr[i].isnumeric():
                temp = ""
                while i < len(abbr) and abbr[i].isnumeric():
                    temp += abbr[i]
                    i +=1
                if temp[0] == "0":
                    return False
                else:
                    ptr += int(temp)
            else:
                if ptr >= len(word) or word[ptr] != abbr[i]:
                    return False
                ptr+=1
                i +=1
        return True if ptr == len(word) else False

                
