class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev1 =0 
        curr1 = 0
        for i in range(0, len(bank)):

            curr = Counter(bank[i])
            curr1 = 0 if "1" not in curr else curr['1']

            ans += prev1*curr1
            if curr1 > 0:
                prev1 = curr1

        return ans
