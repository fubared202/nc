class Solution:
    GRID_SIZE = 9
    BOX_SIZE = 3

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # First validate the rows.
        for i in range(0, self.GRID_SIZE):
            check_list = [False] * self.GRID_SIZE
            for j in range(0, self.GRID_SIZE):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    if not check_list[num-1]:
                        check_list[num-1] = True
                    else:
                        return False

        # Now the columns
        for i in range(0, self.GRID_SIZE):
            check_list = [False] * self.GRID_SIZE
            for j in range(0, self.GRID_SIZE):
                if board[j][i] != ".":
                    num = int(board[j][i])
                    if not check_list[num-1]:
                        check_list[num-1] = True
                    else:
                        return False

        # Finally, the boxes.
        for box_num in range(0, self.GRID_SIZE):
            check_list = [False] * self.GRID_SIZE
            box_start_x = (box_num % self.BOX_SIZE) * self.BOX_SIZE 
            box_start_y = int(box_num / self.BOX_SIZE) * self.BOX_SIZE
            for i in range(0, self.BOX_SIZE):
                for j in range(0, self.BOX_SIZE):
                    if board[box_start_x + i][box_start_y + j] != ".":
                        num = int(board[box_start_x + i][box_start_y + j])
                        if not check_list[num-1]:
                            check_list[num-1] = True
                        else:
                            return False

        return True