import string

def valid_move(board: list[list[str]], p: str, y: int, x: int, flip: bool = False) -> bool:
    opp = 'X' if p == 'O' else 'O'
    if y >= len(board) or x >= len(board):
        return False
    for dir_i in range(-1,2):
        for dir_j in range(-1,2):
            if not dir_i == 0 or not dir_j == 0:
                temp_i = y + dir_i
                temp_j = x + dir_j
                if board[y][x] == '.':
                    while temp_i >= 0 and temp_i < len(board) and temp_j >= 0 and temp_j < len(board) and board[temp_i][temp_j] == opp:
                        temp_i += dir_i
                        temp_j += dir_j
                        if temp_i >= 0 and temp_i < len(board) and temp_j >= 0 and temp_j < len(board) and board[temp_i][temp_j] == p:
                            if flip == True:
                                while not(temp_i == y and temp_j == x):
                                    #print(dir_j, dir_j)
                                    #print(chr(temp_j+65)+str(temp_i+1))
                                    board[temp_i][temp_j] = p
                                    temp_i -= dir_i
                                    temp_j -= dir_j
                            else:
                                return True
    if flip == True:
        board[y][x] = p
        return None
    else:
        return False



'''def pos_has_move(board: list[list[str]], p: str, opp: str, i, j, dir_i = 0, dir_j = 0) -> bool:
    temp_i = i + dir_i
    temp_j = j + dir_j
    while temp_i >= 0 and temp_i < len(board) and temp_j >= 0 and temp_j < len(board) and board[temp_i][temp_j] == opp:
        temp_i += dir_i
        temp_j += dir_j
        if board[temp_i][temp_j] == p:
            return True
    return False'''
    

         
def has_valid_moves(board: list[list[str]], p: str) -> bool:
    opp = 'X' if p == 'O' else 'O'
    valid_move_pos = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '.':
                """
                for dir_i in range(-1,2):
                    for dir_j in range(-1, 2):
                        if not dir_i == 0 or not dir_j == 0:
                            if pos_has_move(board, "X", "O", i, j, dir_i, dir_j):
                                valid_move_pos.append((i,j))"""
                if valid_move(board, p, i, j, flip=False):
                    valid_move_pos.append(chr(j+65)+str(i+1))
                    #return True                 
    #print(valid_move_pos)
    if valid_move_pos:
        return True
    return False   

def has_empty_cell(board: list[list[str]]) -> bool:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '.':
                return True
    return False

def main() -> None:
    board_size = int(input("Enter board size: "))

    global board
    board = [['.']*board_size for i in range(board_size)]                       #Create board
    

    board[board_size//2][board_size//2] = board[board_size//2 - 1][board_size//2 - 1] = "X"     #initialize the 4 central cells
    board[board_size//2][board_size//2 - 1] = board[board_size//2 - 1][board_size//2] = "O"

    #print_board(board)


    block_number = int(input("Enter number of blocks: "))       #Enter the number of blocks
    while block_number > ((board_size*board_size) / 2):  
        print("Too many blocks!")       
        block_number = int(input("Enter number of blocks: "))

    for i in range(block_number):                               #Enter the position of blocks
        pos = input(f"Enter position of block {i+1}: ")
        y, x = ord(pos[0].upper())-65, int(pos[1:])-1
        while max(x, y) >= board_size or min(x, y) < 0 or not board[x][y] == '.':       #check the validity of inputted cell
            print("Invalid position!")
            pos = input(f"Enter position of block {i+1}: ")
            y, x = ord(pos[0].upper())-65, int(pos[1:])-1
        board[x][y] = '#'

    #print_board(board)

    #print(has_valid_moves(board, "X"))

    #Player take turn
    ind_round = 1 
    p = "X"
    previous_no_move = False
    while has_empty_cell(board):
        print(f"Round {ind_round}:")
        print_board(board)
        if has_valid_moves(board, p):
            previous_no_move = False
            next_pos = input(f"Player {p}'s turn: ")
            y, x = ord(next_pos[0].upper())-65, int(next_pos[1:])-1
            while not  valid_move(board, p, x, y):
                print('Invalid move')
                next_pos = input(f"Player {p}'s turn: ")
                y, x = ord(next_pos[0].upper())-65, int(next_pos[1:])-1
            valid_move(board, p, x, y, flip=True)
        else:
            print(f"Player {p} has no vlid moves! Pass!")
            if previous_no_move == True:
                game_over(board)
                exit()
            previous_no_move = True
        
        ind_round += 1
        p = "X" if p == "O" else "O"
    game_over(board)
    #Win or Draw

def game_over(board):
    print(f"Game over:")
    print_board(board)
    num_X = 0
    num_O = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "X":
                num_X += 1
            elif board[i][j] == "O":
                num_O += 1
    if num_O > num_X:
        print("Player O wins")
    elif num_X > num_O:
        print("player X wins")
    elif num_O == num_X:
        print("Draw game!")

def print_board(board: list[list[str]]):
    count = 0
    print('   ', end='')
    for i in string.ascii_uppercase:
        if count >= len(board):
            break
        print(i, end=' ')
        count += 1
    print()
    count = 1
    for i in board:
        if count < 10:
            print(' ', end='')
        print(count, end=' ')
        for j in i:
            print(j, end=' ')
        print(' ')
        count += 1


if __name__ == "__main__":
    main()
    