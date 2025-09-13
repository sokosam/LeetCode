class Solution:
    def maxFreqSum(self, s: str) -> int:
        chars = [0]*26

        for i in s:
            index = ord(i) - ord('a')
            chars[index] +=1
        
        bestVowel = 0
        bestConst = 0

        vowels = {'a', 'e', 'i','o','u'}
        vowelIndexes = set([ord(i) - ord('a') for i in vowels])

        for i in range(len(chars)):
            if i in vowelIndexes:
                bestVowel = max(bestVowel, chars[i])
            else:
                bestConst = max(bestConst, chars[i])

        return bestVowel + bestConst