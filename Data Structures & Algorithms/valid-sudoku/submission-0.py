from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                d = int(val)  
                mask = 1 << (d - 1)

     
                if rows[i] & mask:
                    return False
                rows[i] |= mask

                if cols[j] & mask:
                    return False
                cols[j] |= mask

                box_index = (i // 3) * 3 + (j // 3)
                if boxes[box_index] & mask:
                    return False
                boxes[box_index] |= mask

        return True
