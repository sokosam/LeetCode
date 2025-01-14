class Solution:
    def minimumLength(self, s: str) -> int:
        m = {}
        for i in s:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        print(m)
        ans = 0
        for i in m:
            if m[i] % 2 == 1:
                ans += 1
            else:
                ans += 2
        return ans


        # aaa aaa aaa
        # a   a   a
        #     a

        # aaa aaa aaa a
        # a   a   a   a
        # a  a

        # aaa aaa aaa aa
        # a  a   a   aa
        # a aa
        # a

