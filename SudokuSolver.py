def solveSudoku(self, board):
    # Initialize helper structures to keep track of used numbers in rows, columns, and boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    # Fill the helper structures with the initial numbers from the board
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != ".":
                num_int = int(num)
                rows[i].add(num_int)
                cols[j].add(num_int)
                box_index = (i // 3) * 3 + j // 3
                boxes[box_index].add(num_int)

    def backtrack(i, j):
        # If we've reached the end of the board, return True
        if i == 9:
            return True
        # Move to the next cell
        next_i, next_j = (i, j + 1) if j < 8 else (i + 1, 0)
        if board[i][j] != ".":
            return backtrack(next_i, next_j)
        else:
            box_index = (i // 3) * 3 + j // 3
            for num in range(1, 10):
                if (
                    num not in rows[i]
                    and num not in cols[j]
                    and num not in boxes[box_index]
                ):
                    # Place the number and update helper structures
                    board[i][j] = str(num)
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)
                    # Recursively attempt to fill the rest of the board
                    if backtrack(next_i, next_j):
                        return True
                    # Backtrack if placing num doesn't lead to a solution
                    board[i][j] = "."
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_index].remove(num)
            return False

    backtrack(0, 0)
