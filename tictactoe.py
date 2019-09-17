def tictactoe():
    end = False
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    win_condition = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8))

    def map():
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])

    def player1():
        n = int(input("Enter a number here: "))
        n = n - 1
        if board[n] == "X" or board[n] == "O":
            print("Someone has already placed something here! ")
        else:
            board[n] = "X"

    def player2():
        n = int(input("Enter a number here: "))
        n = n - 1
        if board[n] == "X" or board[n] == "O":
            print("Someone has already placed something here: ")
        else:
            board[n] = "O"

    def boardstate():
        for i in win_condition:
            if board[i[0]] == board[i[1]] == board[i[2]] == "X":
                print("Player 1 wins")
                return True
            if board[i[0]] == board[i[1]] == board[i[2]] == "O":
                print("Player 2 wins")
                return True
            if board.count("X") == 4 and board.count("O") == 5:
                print("Its a tie")
                return True
            if board.count("X") == 5 and board.count("O") == 4:
                print("Its a tie")
                return True
            else:
                continue


    while not end:
        map()
        end = boardstate()
        if end == True:
            break
        print("Where do you want to place an X? ")
        player1()
        map()
        end = boardstate()
        if end == True:
            break
        print("Where do you want to place an O? ")
        player2()
        end = boardstate()
        if end == True:
            break
tictactoe()
