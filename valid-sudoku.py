from collections import defaultdict

def solution(board):
    row_set = defaultdict(set)
    col_set = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in row_set[r]) or (board[r][c] in col_set[c]) or (board[r][c] in squares[(r // 3, c // 3)]):
                return False
            row_set[r].add(board[r][c])
            col_set[c].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True

if __name__ == "__main__":
    sol = solution([[".",".","4",".",".",".","6","3","."]
                    ,[".",".",".",".",".",".",".",".","."]
                    ,["5",".",".",".",".",".",".","9","."]
                    ,[".",".",".","5","6",".",".",".","."]
                    ,["4",".","3",".",".",".",".",".","1"]
                    ,[".",".",".","7",".",".",".",".","."]
                    ,[".",".",".","5",".",".",".",".","."]
                    ,[".",".",".",".",".",".",".",".","."]
                    ,[".",".",".",".",".",".",".",".","."]])
    print(sol)