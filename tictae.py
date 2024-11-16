from tkinter import *
#create main windows
windows = Tk()
windows.title("Tic Tac Toe game")
windows.geometry("400x500")

windows.resizable(0,0)

frame1 = Frame(windows)
frame1.pack()
titleLabel = Label(frame1 , text="Tic Tac Toe" , font=("Arial Rounded MT Bold" , 26) , bg="yellow" , width=16 )
titleLabel.grid(row=0 , column=0)


frame2 = Frame(windows , bg="black")
frame2.pack()

optionFrame = Frame(windows , bg="grey")
optionFrame.pack()



board = {i: " " for i in range(1, 10)}
turn = "x"
endGame = False
mode = "singlePlayer"

def setMode(new_mode):
    global mode
    mode = new_mode
    updateButtonColors()

def updateButtonColors():
    if mode == "singlePlayer":
        singlePlayerButton.config(bg="lightgreen")
        twoPlayerButton.config(bg="lightgrey")
    elif mode == "twoPlayer":
        singlePlayerButton.config(bg="lightgrey")
        twoPlayerButton.config(bg="lightgreen")

def SingleMode(): 
    setMode("singlePlayer")

def twoPlayerMode():
    setMode("twoPlayer")


def updateBoard():
    for key, value in board.items():
        buttons[key - 1].config(text=value)


def checkWin(player):

    win_conditions = [
        [1, 2, 3],  # 1st row
        [4, 5, 6],  # 2nd row
        [7, 8, 9],  # 3rd row
        [1, 4, 7],  # 1st col
        [2, 5, 8],  # 2nd col
        [3, 6, 9],  # 3rd col
        [1, 5, 9],  # đường chéo chính
        [3, 5, 7]   # đường chéo phụ
    ]

    # check win conditions
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True

    return False


def checkDraw():
    return all(value != " " for value in board.values())

def resetTitle():
    titleLabel = Label(frame1 , text="Tic Tac Toe" , font=("Arial Rounded MT Bold" , 30) , bg="yellow" , width=15 )
    titleLabel.grid(row=0 , column=0)

def resetButton():
    for button in buttons:
        button["text"] = " "

def resetBoard():
    for key in board:
        board[key] = " "

def restartGame():
    global endGame
    endGame = False
    resetButton()

    resetBoard()

    resetTitle()

def minimax(board, isMaximizing):
    result = evaluateBoard()
    if result is not None:
        return result

    if isMaximizing:
        bestScore = -float('inf')
        player = "o"
        nextIsMaximizing = False
    else:
        bestScore = float('inf')
        player = "x"
        nextIsMaximizing = True

    for key in board.keys():
        if board[key] == " ":
            board[key] = player
            score = minimax(board, nextIsMaximizing)
            board[key] = " "
            if isMaximizing:
                bestScore = max(score, bestScore)
            else:
                bestScore = min(score, bestScore)

    return bestScore

def evaluateBoard():
    if checkWin("o"):
        return 1
    if checkWin("x"):
        return -1
    if checkDraw():
        return 0
    return None


def playComputer():
    bestScore = -100
    bestMove = None

    # Duyệt qua tất cả các ô trên bảng
    for position, value in board.items():
        if value == " ":
            # Thử đặt 'o' vào ô trống
            board[position] = "o"
            score = minimax(board, False)  # Gọi hàm minimax để tính điểm
            # Hoàn tác nước đi
            board[position] = " "
            # Cập nhật nước đi tốt nhất
            if score > bestScore:
                bestScore = score
                bestMove = position

    # Thực hiện nước đi tốt nhất
    if bestMove is not None:
        board[bestMove] = "o"
        updateBoard()

#  play
def play(event):
    global turn,endGame
    if endGame:
        return
    
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]
    if clicked == "n" :
        clicked = 1
    else :
        clicked = int(clicked)
    
    if button["text"] == " ":
        if turn == "x" :
            board[clicked] = turn
            if checkWin(turn):
                winningLabel = Label(frame1 , text=f"{turn} wins the game", bg="red", font=("Arial Rounded MT Bold" , 26),width = 16 )
                winningLabel.grid(row = 0 , column = 0 , columnspan = 3)
                endGame = True

            turn = "o"

            updateBoard()

            if mode == "singlePlayer":

                playComputer()

                if checkWin(turn):
                    winningLabel = Label(frame1 , text=f"{turn} wins the game", bg="green", font=("Arial Rounded MT Bold" , 26),width = 16   )
                    winningLabel.grid(row = 0 , column = 0 , columnspan=3)
                    endGame = True

                turn = "x"

                updateBoard()

        else:
            board[clicked] = turn
            updateBoard()
            if checkWin(turn):
                winningLabel = Label(frame1 , text=f"{turn} wins the game" , bg="green", font=("Arial Rounded MT Bold" , 26),width=16)
                winningLabel.grid(row = 0 , column=0 , columnspan=3)
                endGame = True
            turn = "x"

        
        if checkDraw():
            drawLabel = Label(frame1 , text=f"Game Draw" , bg="red", font=("Arial Rounded MT Bold" , 26), width = 16)
            drawLabel.grid(row = 0 , column=0 , columnspan=3)
        

# ------ UI --------

# Change Mode options 

singlePlayerButton = Button(optionFrame , text="Single player Mode" , width=13 , height=1 , font=("Arial Rounded MT Bold" , 15) , bg="lightgrey" , relief=RAISED , borderwidth=5 , command=SingleMode)
singlePlayerButton.grid(row=0 , column=0 , columnspan=1 , sticky=NW)

twoPlayerButton = Button(optionFrame , text="2-player mode" , width=13 , height=1 , font=("Arial Rounded MT Bold" , 15) , bg="lightgrey" , relief=RAISED , borderwidth=5 , command=twoPlayerMode )
twoPlayerButton.grid(row=0 , column=1 , columnspan=1 , sticky=NW)

# Tic Tac Toe 

buttons = []

# create button with loop
for i in range(9):
    button = Button(
        frame2, 
        text=" ", 
        width=4, 
        height=2, 
        font=("Arial Rounded MT Bold", 30), 
        bg="yellow", 
        relief=RAISED, 
        borderwidth=5
    )
    button.grid(row=i//3, column=i%3)
    button.bind("<Button-1>", play)
    buttons.append(button)

# Nút Restart Game
restartButton = Button(
    frame2, 
    text="Restart Game", 
    width=19, 
    height=1, 
    font=("Arial Rounded MT Bold", 20), 
    bg="Green", 
    relief=RAISED, 
    borderwidth=5, 
    command=restartGame
)
restartButton.grid(row=4, column=0, columnspan=3)


windows.mainloop()