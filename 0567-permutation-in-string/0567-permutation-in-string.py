class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) == len(s2):
            return sorted(s1) == sorted(s2)


        smaller = s1
        bigger = s2

        # if len(s1) > len(s2):
        #     smaller = s2
        #     bigger = s1

        
        count = Counter(s1)

        start = 0
        m = defaultdict(int)

        for end in range(len(s2)):

            m[s2[end]] += 1
            if end >= len(s1):
                m[s2[start]] -=1
                start +=1
            
            accepted = True
            for i in count:
                if count[i] != m[i]:
                    accepted= False
            if accepted:
                return True
            end+=1
        return False
        