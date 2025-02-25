class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        negative = 0

        if dividend < 0:
            negative ^= 1
        if divisor < 0:
            negative ^= 1
        print(negative)

        

        
        dividend = abs(dividend)
        divisor = abs(divisor)

        count = 0
        prev = 0
        if dividend >= divisor:
            count += 1
            dividend -= divisor
            prev = 1

        temp = divisor
        
        while dividend >= temp + temp:
            prev = prev + prev
            count += prev
            dividend -= temp + temp
            temp += temp

        while dividend >= divisor:
            count +=1
            dividend -= divisor

        if count >= 2147483647 and not negative:
            return 2147483647
        elif count >= 2147483648 and negative:
            return -2147483648
        
        return count if not negative else 0 - count