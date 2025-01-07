class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x : len(x))
        ans =[]

        for i in range(len(words)):
            for j in range(i +1, len(words)):
                print(words[i], words[j])
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans
            