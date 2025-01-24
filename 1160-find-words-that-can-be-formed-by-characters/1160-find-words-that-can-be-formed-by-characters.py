class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        count = [0 for _ in range(26)]
        
        for i in chars:
            count[ord(i) - ord('a')] += 1
            
        ans =0
        for word in words:
            vals = [0] * 26
            passed = True
            for i in word:
                vals[ord(i) - ord('a')] +=1
                if vals[ord(i) - ord('a')] > count[ord(i) - ord('a')]:
                    passed = False
            if passed:
                ans += len(word)
                
        return ans