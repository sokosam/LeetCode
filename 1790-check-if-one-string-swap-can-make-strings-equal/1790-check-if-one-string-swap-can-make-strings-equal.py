class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
    
        disc = -1

        # countDisc = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                # countDisc +=1
                if disc == -1:
                    disc = i
                elif disc == -2:
                    return False
                else:
                    if s1[disc] != s2[i] or s2[disc] != s1[i]:
                        return False
                    else:
                        disc = -2
        return True if disc < 0 else False
