class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:



            """

            > < > 

            < > <


            > < > < > < <

            [1,-1,1,-1,1]


            """
            arr2 = []

            for i in range(1,len(arr)):
                if arr[i] > arr[i -1]:
                    arr2.append(-1)
                elif arr[i] == arr[i-1]:
                    arr2.append(0)
                else:
                    arr2.append(1)


            prev = -2
            best = 0
            consec = 0
            for i in arr2:   
                if i == 0:
                    consec =0
                elif prev + i == 0:
                    consec +=1
                else:
                    consec = 1
                prev = i
                best = max(best, consec)
            return best + 1


                