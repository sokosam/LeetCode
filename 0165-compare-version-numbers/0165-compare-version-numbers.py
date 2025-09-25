class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split('.')

        for i in range(len(v1)):
            curr = v1[i]
            l =0 
            while l < len(curr) and curr[l] == "0":
                l +=1

            v1[i]= curr[l:]
            if l >= len(curr):
                v1[i] = "0"
        for i in range(len(v2)):
            curr = v2[i]
            l =0 
            while l < len(curr) and curr[l] == "0":
                l +=1

            v2[i]= curr[l:]
            if l >= len(curr):
                v2[i] = "0"
        # print(v1,v2)


        for i in range(min(len(v1), len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif  int(v1[i]) < int(v2[i]):
                return -1
        
        for i in range(min(len(v1), len(v2)), max(len(v1) , len(v2))):
            if i < len(v1):
                if int(v1[i]) != 0:
                    return 1
            else:
                if int(v2[i]) != 0:
                    return -1
        return 0




            