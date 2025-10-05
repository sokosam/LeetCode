class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """



        w < r < t
        w < r < f
        e < r
        e < t == t
        r < f < t ==t 

        e < r < f <t
        """

        adj = [set() for _ in range(26)]
        cnt = [-1]*26


        def compareTwoWords(w1,w2):
            minLen = min(len(w1),len(w2))

            for i in range(minLen):
                if w1[i] == w2[i]:
                    continue
                else:
                    index1 = ord(w1[i]) - ord('a')
                    index2 = ord(w2[i]) - ord('a')
                    if cnt[index1] == -1:
                        cnt[index1] = 0
                    if cnt[index2] == -1:
                        cnt[index2] = 0
                    if index2 not in adj[index1]:
                        adj[index1].add(index2)
                        cnt[index2] +=1
                    return True
            if len(w1) > len(w2):
                return False
            return True
            
                

        for i in range(len(words)):
            for char in words[i]:
                index1 = ord(char) - ord('a')
                if cnt[index1] == -1:
                    cnt[index1] = 0


            for j in range(i + 1, len(words)):
                if not compareTwoWords(words[i], words[j]):
                    return ""
        q = deque()

        for i in range(len(cnt)):
            if cnt[i] == 0:
                q.append(i)
        ans = ""
        while q:
            curr = q.popleft()
            character = chr(curr + ord('a'))

            ans += character

            # print([chr(i + ord('a')) for i in adj[curr]])
            for i in adj[curr]:
                cnt[i] -=1
                if cnt[i] == 0:
                    q.append(i)

        if all([i == -1 for i in cnt]):
            if len(words) > 0:
                return words[-1]
        # print(ans)
        for i in cnt:
            if i > 0:
                return ""
        return ans

                    