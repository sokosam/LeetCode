class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        words2 = [sorted(i) for i in words]

        ans = [words[0]]

        for i in range(1,len(words)):
            if words2[i] != words2[i - 1]:
                ans.append(words[i])
        return ans