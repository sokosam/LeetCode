class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        """

        # of intergers > 2 

        their summation of (x-2 ) %2 == 1

        alice will the game
        """




        consecAs = 0
        consecBs = 0
        aliceMoves = 0
        bobMoves = 0
        for i in colors:
            if i == "A":
                bobMoves += max(0, consecBs - 2)
                consecAs += 1
                consecBs = 0
            if i == "B":
                aliceMoves += max(0, consecAs - 2)
                consecBs +=1
                consecAs = 0
        aliceMoves += max(0, consecAs - 2)
        bobMoves += max(0, consecBs - 2)
        print(aliceMoves,bobMoves)
        return aliceMoves > 0 and aliceMoves >= bobMoves + 1


    # def test(colors, answer):
    #     assert self.winnerOfGame(colors) == answer

    