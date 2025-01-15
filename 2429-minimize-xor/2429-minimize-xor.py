class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        """

        0011

        0101

        


        """

        def countSet(x):
            count = 0
            while x > 0:
                count += x & 1
                x = x >> 1
            return count

        allowedBits =  countSet(num2) - countSet(num1)
        
        if allowedBits == 0:
            return num1
        elif allowedBits > 0:
            temp = num1
            ans = 0
            exp = 0
            curr = 0
            while curr < allowedBits:
                lsb = num1 & 1
                num1 = num1 >> 1
                if lsb:
                    exp += 1
                    continue
                else:
                    ans += 2**exp  
                    exp +=1
                    curr +=1
            return ans + temp

        elif allowedBits < 0:  
            temp =num1
            allowedBits = -allowedBits
            ans = 0
            exp = 0
            curr = 0
            while curr < allowedBits:
                lsb = num1 & 1

                num1 = num1 >> 1
                if lsb:
                    ans += 2**exp
                    exp += 1
                    curr +=1
                    continue
                else: 
                    exp +=1

            return temp - ans
        
        
            

# 1000001

# 1010100




#   11001

#   11000