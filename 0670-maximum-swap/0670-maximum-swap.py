class Solution:
    def maximumSwap(self, num: int) -> int:
        #1 9 9 3
        # 9 9 1 3
        # num = 1993
        s = str(num)
        l = [ x for x in s]
        l.sort(reverse = True)
        # print(l)
        right = 0
        left =  0
        # print(s , l)
        for i in range(len(s)):
            if s[i] != l[i]:
                left = i
                right = len(s ) - 1
                while right >= 0:
                    if s[right] != l[i]:
                        right -= 1
                    else:
                        break
                break
        # print(left, right)
        # print(s[right])
        ans = []
        for i in range(len(s)):
            if i == left:
                ans.append(s[right])
            elif i == right:
                ans.append(s[left])
            else:
                ans.append(s[i])
        
        return int("".join(ans))

        # return int(s)