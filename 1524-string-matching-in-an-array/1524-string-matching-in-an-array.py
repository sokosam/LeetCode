class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key = lambda x : len(x))
        count = 0
        ans =[]

        for i in range(len(words)):
            for j in range(i +1, len(words)):
                if words[i] in words[j]:
                    words[count] = words[i]
                    count += 1
                    break
        del words[count :]
        return words
            