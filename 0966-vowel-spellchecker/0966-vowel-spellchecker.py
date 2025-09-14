class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        m = set()
        caseIn = {}
        vowels = {}


        for word in wordlist:
            m.add(word)
            if word.lower() not in caseIn:
                caseIn[word.lower()] = word
            temp = []
            for i in word.lower():
                if i in "aeiou":
                    temp.append("*")
                else:
                    temp.append(i)
            temp = "".join(temp)
            if temp not in vowels:
                vowels[temp] = word
        
        ans = []
        for query in queries:
            if query in m:
                ans.append(query)
            elif query.lower() in caseIn:
                ans.append(caseIn[query.lower()])
            else:
                temp = []
                for i in query.lower():
                    if i in "aeiou":
                        temp.append("*")
                    else:
                        temp.append(i)
                temp = "".join(temp)
                if temp in vowels:
                    ans.append(vowels[temp])
                else:
                    ans.append("")
        return ans
