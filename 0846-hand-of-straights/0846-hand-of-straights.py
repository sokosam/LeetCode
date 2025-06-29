class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        m = Counter(hand)
        c = list(set(hand))
        c.sort()
        # print(c)

        for card in c:
            count = m[card]
            if count == 0:
                continue
            m[card] = 0
            for k in range(1, groupSize):
                if card + k not in m or m[card +k] < count:
                    # print(m, card, card + k)
                    return False
                else:
                    m[card + k] -= count
        return True


