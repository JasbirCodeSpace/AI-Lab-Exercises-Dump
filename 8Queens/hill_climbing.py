

# import libraries
import random

# global variables
N = 8

def configureRandomly(board, state):
    for i in range(N):
        state[i] = random.randint(0, N - 1)
        board[state[i]][i] = 1

def printBoard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end = " ")
        print()

def printState(state):
    for i in range(N):
        print(state[i], end = " ")

def compareStates(state1, state2):
    for i in range(N):
        if state1[i] != state2[i]:
            return False
    return True

def fill(board, value):
    for i in range(N):
        for j in range(N):
            board[i][j] = value

def calculateObjective(board, state):
    attacking = 0
    row, col = 0, 0

    for i in range(N):

        row = state[i]
        col = i - 1
        while col >= 0 and board[row][col] != 1:
            col -= 1
        if col >= 0 and board[row][col] == 1:
            attacking += 1
        
        row = state[i]
        col = i + 1
        while col < N and board[row][col] != 1:
            col += 1
        if col < N and board[row][col] == 1:
            attacking += 1
        
        row = state[i] - 1
        col = i - 1
        while row >= 0 and col >= 0 and board[row][col] != 1:
            row -= 1
            col -= 1
        if row >= 0 and col >= 0 and board[row][col] == 1:
            attacking += 1
        
        row = state[i] + 1
        col = i + 1
        while col < N and row < N and board[row][col] != 1:
            col += 1
            row += 1
        if col < N and row < N and board[row][col] == 1:
            attacking += 1

        row = state[i] + 1
        col = i - 1
        while col >= 0 and row < N and board[row][col] != 1:
            col -= 1
            row += 1
        if col >= 0 and row < N and board[row][col] == 1:
            attacking += 1
        
        row = state[i] - 1
        col = i + 1
        while col < N and row >= 0 and board[row][col] != 1:
            row -= 1
            col += 1
        if col < N and row >= 0 and board[row][col] == 1:
            attacking += 1
    
    return int(attacking/2)

def generateBoard(board, state):
    fill(board, 0)
    for i in range(N):
        board[state[i]][i] = 1

def copyState(state1, state2):
    for i in range(N):
        state1[i] = state2[i]

def getNeighbour(board, state):
    optBoard = [[0] * N for i in range(N)]
    optState = [0 for i in range(N)]

    copyState(optState, state)
    generateBoard(optBoard, optState)

    optObjective = calculateObjective(optBoard, optState)

    neighbourBoard = [[0] * N for i in range(N)]
    neighbourState = [0 for i in range(N)]

    copyState(neighbourState, state)
    generateBoard(neighbourBoard, neighbourState)

    for i in range(N):
        for j in range(N):

            if j != state[i]:
                neighbourState[i] = j
                neighbourBoard[neighbourState[i]][i] = 1
                neighbourBoard[state[i]][i] = 0

            temp = calculateObjective(neighbourBoard, neighbourState)

            if temp <= optObjective:
                optObjective = temp
                copyState(optState, neighbourState)
                generateBoard(optBoard, optState)

            neighbourBoard[neighbourState[i]][i] = 0
            neighbourState[i] = state[i]
            neighbourBoard[state[i]][i] = 1

    copyState(state, optState)
    fill(board, 0)
    generateBoard(board, state)

def hillClimbingHelper(board, state, neighbourBoard, neighbourState):
    copyState(state, neighbourState)
    generateBoard(board, state)

    getNeighbour(neighbourBoard, neighbourState)

    if compareStates(state, neighbourState):
        printBoard(board)
        return True
    
    elif calculateObjective(board, state) == calculateObjective(neighbourBoard, neighbourState):
        neighbourState[random.randint(0, N - 1)] = random.randint(0, N - 1)
        generateBoard(neighbourBoard, neighbourState)

    return False

def hillClimbing(board, state):

    neighbourBoard = [[0] * N for i in range(N)]
    neighbourState = [0 for i in range(N)]

    copyState(neighbourState, state)
    generateBoard(neighbourBoard, neighbourState)

    res = hillClimbingHelper(board, state, neighbourBoard, neighbourState)
    if res == True:
        return

    while True:
        res = hillClimbingHelper(board, state, neighbourBoard, neighbourState)
        if res == True:
            break

if __name__ == "__main__":
    state = [0 for i in range(N)]
    board = [[0] * N for i in range(N)]

    configureRandomly(board, state)
    hillClimbing(board, state)