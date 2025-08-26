class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        ans = []
        curr = []
        used = 0
        
        def format(words, width, used):
            if len(words) == 1:
                return words[0] + " "*(width - len(words[0]))
            breaks = len(words) - 1
            spaces = width - used
            spaceLength = spaces//breaks
            leftover = spaces % breaks
            # print(width, used, breaks,spaces, leftover)
            ans = ""
            for i in range(len(words)):
                if i == len(words) - 1:
                    ans += words[i]
                else:
                    ans += words[i]
                    if leftover > 0:
                        
                        ans += " "
                        leftover -=1
                    ans += " "*spaceLength
            return ans




        for word in words:
            if maxWidth - used - len(curr) - len(word)>= 0:
                used += len(word)
                curr.append(word)
            else:
                ans.append(format(curr,maxWidth,used))
                curr = [word]
                used = len(word)
        ans.append(" ".join(curr) + " "*(maxWidth - used - len(curr) + 1))


        return ans
