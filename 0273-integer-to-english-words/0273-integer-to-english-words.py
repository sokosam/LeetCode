class Solution:
    def numberToWords(self, num: int) -> str:
        print(2**31 - 1)

        num_to_eng = {
            0 : "Zero",
            1 : "One",
            2 : "Two",
            3 : "Three",
            4 : "Four",
            5 : "Five",
            6 : "Six",
            7 : "Seven",
            8 : "Eight",
            9 : "Nine",
            10 : "Ten",
            11 : "Eleven",
            12 : "Twelve",
            13 : "Thirteen",
            14 : "Fourteen",
            15 : "Fifteen",
            16 : "Sixteen",
            17 : "Seventeen",
            18 : "Eighteen",
            19 : "Nineteen",
            20 : "Twenty",
            30 : "Thirty",
            40 : "Forty",
            50 : "Fifty",
            60 : "Sixty",
            70 : "Seventy",
            80 : "Eighty",
            90 : "Ninety",
        }
        def twoDigit(n):
            if n in num_to_eng:
                return num_to_eng[n]
            first_digit = n%10
            str_val = num_to_eng[first_digit]
            second_digit = n - first_digit
            if second_digit == 0:
                return str_val
            str_val_two = num_to_eng[second_digit]
            return str_val_two + " " + str_val

        def threeDigit(n):
            if n in num_to_eng:
                return num_to_eng[n]
            two_val = twoDigit(n%100)
            third_digit = n//100
            if third_digit == 0:
                return two_val
            if n%100 == 0:
                return num_to_eng[third_digit] + " Hundred"
            return num_to_eng[third_digit] + " Hundred " + two_val

        running_string = ""
        iteration = 0
        buckets = ["", " Thousand", " Million", " Billion"]
        if num == 0:
            return "Zero"
        while num > 0:
            working_num = num%1000
            if working_num == 0:
                iteration += 1
                num //= 1000
                continue
            value = threeDigit(working_num)
            value += buckets[iteration]
            
            if len(running_string) > 0:
                running_string = value + " " +  running_string
            else:
                running_string = value
            iteration += 1
            num//= 1000
        return running_string




