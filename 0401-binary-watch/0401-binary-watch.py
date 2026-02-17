class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        bitsRequired = [0]*60

        for i in range(60):
            setBits = 0

            k = i
            while k > 0:
                setBits += k & 1
                k>>=1 

            bitsRequired[i] = setBits
        

        ans = []

        minutes_only = []
        hours = []

        for i in range(60):
            if bitsRequired[i] == turnedOn:
                minutes = str(i)
                if len(minutes) == 1:
                    minutes = "0" + minutes
                x= "0:"+ str(minutes)
                minutes_only.append(x)
        

        for i in range(1,12):

            hour =  str(i)

            bits_used = bitsRequired[i]

            for i in range(60):
                if bitsRequired[i] +bits_used == turnedOn:
                    minutes = str(i)
                    if len(minutes) == 1:
                        minutes = "0" + minutes
                    x= hour + ":" + minutes
                    hours.append(x)
        
        return minutes_only + hours