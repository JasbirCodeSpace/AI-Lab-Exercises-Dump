
start, end, solutions = [], [], []

def move(state,action):

     if state[2] == 1:
         return [state[i] - action[i] for i in range(3)]
     else:
         return [state[i] + action[i] for i in range(3)]

def isLegal(state):

     if 0 <= state[0] <= N and 0 <= state[1] <= N:
         return True
     else:
         return False

def isBankSafe(bank):

     if bank[1] <= bank[0] or bank[0] == 0:
         return True
     else:
         return False

def isStateSafe(LeftBankState):

     rightBankState = [start[i]-LeftBankState[i] for i in range(3)]
     if isBankSafe(LeftBankState) and isBankSafe(rightBankState) :
         return True
     else:
         return False

def nextPossibleMoves(state):

     movesList = []

     for i in range(N):
         for j in range(N):
             if ((i == 0 and j != 0 ) or (i != 0 and i >= j)) and (i + j) <= x:
                 movesList.append([i,j,1])

     moves = []
     for i in movesList:

         j = move(state,i)
         if isLegal(j) and isStateSafe(j):
             moves.append(j)
     return moves

def generateSolutions(nextState,curPath):

     solPath = curPath.copy()

     if nextState == end:
         curPath.append(nextState)
         solutions.append(solPath)
         return

     elif nextState in curPath:
         return

     else:
         solPath.append(nextState)

         for i in nextPossibleMoves(nextState):
             generateSolutions(i,solPath)

def printSolution(solutions):

    print("\nPossible way to solve for final state :- ",end= "\n\n")
    counter = 0

    for path in solutions:

        print(f"Solution {counter + 1}")
        print("[ ",end = "")

        for state in path:
            print("{} -> ".format(state),end = "")

        print("{} ]".format(end),end = "\n\n")
        counter += 1


if __name__ == "__main__":

    N = int(input("Enter the value for N: "))
    x = int(input("Enter the value for x: "))
    start = [N,N,1]
    end = [0,0,0]
    generateSolutions(start,[])
    printSolution(solutions)
