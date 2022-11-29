from copy import deepcopy

n = 3
class RiverBankState:

    def __init__(self, cannibals, missionaries):
        self.cannibals = cannibals
        self.missionaries = missionaries

    def isValidCoast(self):
        '''
            if the number of missionaries is not outnumbered by the cannibals count or 
            there are no missionaries on the coast, only then the given coast state is valid
        '''
        if self.missionaries >= self.cannibals or self.missionaries == 0:
            return True
        else:
            return False

    def isGoalCoast(self):
        '''
            if all the missionaries and cannibals are on the same side (same coast) then the state is the goal state
        '''
        if self.cannibals == n and self.missionaries == n:
            return True
        else:
            return False

class ProblemState:
    
    def __init__(self, data):
        self.data = data
        self.parent = None
    
    def constructTree(self):
            
        children = []
        current_coast, next_coast = "", ""
        temp = deepcopy(self.data)

        if self.data["boat"] == "left":
            current_coast = "left"
            next_coast = "right"

        elif self.data["boat"] == "right":
            current_coast = "right"
            next_coast = "left"

        # 2 cannibals crossing the river
        if temp[current_coast].cannibals >= 2:
            temp[current_coast].cannibals = temp[current_coast].cannibals - 2
            temp[next_coast].cannibals = temp[next_coast].cannibals + 2
            temp["boat"] = next_coast
            if temp[current_coast].isValidCoast() and temp[next_coast].isValidCoast():
                child = ProblemState(temp)
                child.parent = self
                children.append(child)

        temp = deepcopy(self.data)

        # 2 missionaries crossing the river
        if temp[current_coast].missionaries >= 2:
            temp[current_coast].missionaries = temp[current_coast].missionaries - 2
            temp[next_coast].missionaries = temp[next_coast].missionaries + 2
            temp["boat"] = next_coast
            if temp[current_coast].isValidCoast() and temp[next_coast].isValidCoast():
                child = ProblemState(temp)
                child.parent = self
                children.append(child)

        temp = deepcopy(self.data)

        # 1 cannibal crossing the river
        if temp[current_coast].cannibals >= 1:
            temp[current_coast].cannibals = temp[current_coast].cannibals - 1
            temp[next_coast].cannibals = temp[next_coast].cannibals + 1
            temp["boat"] = next_coast
            if temp[current_coast].isValidCoast() and temp[next_coast].isValidCoast():
                child = ProblemState(temp)
                child.parent = self
                children.append(child)

        temp = deepcopy(self.data)
        
        # 1 missionary crossing the river
        if temp[current_coast].missionaries >= 1:
            temp[current_coast].missionaries = temp[current_coast].missionaries - 1
            temp[next_coast].missionaries = temp[next_coast].missionaries + 1
            temp["boat"] = next_coast
            if temp[current_coast].isValidCoast() and temp[next_coast].isValidCoast():
                child = ProblemState(temp)
                child.parent = self
                children.append(child)

        temp = deepcopy(self.data)
        
        # 1 cannibal and 1 missionary crossing the river
        if temp[current_coast].missionaries >= 1 and temp[current_coast].cannibals >= 1:
            temp[current_coast].missionaries = temp[current_coast].missionaries - 1
            temp[next_coast].missionaries = temp[next_coast].missionaries + 1
            temp[current_coast].cannibals = temp[current_coast].cannibals - 1
            temp[next_coast].cannibals = temp[next_coast].cannibals + 1
            temp["boat"] = next_coast
            if temp[current_coast].isValidCoast() and temp[next_coast].isValidCoast():
                child = ProblemState(temp)
                child.parent = self
                children.append(child)
                
        return children

def bfs():
    left = RiverBankState(n, n)
    right = RiverBankState(0, 0)
    root_data = {"left": left, "right": right, "boat": "left"}

    visited = []
    nodes = []
    path = []
    nodes.append(ProblemState(root_data))

    while len(nodes) > 0:
        g = nodes.pop(0)
        visited.append(g)
        if g.data["right"].isGoalCoast():
            path.append(g)
            return g
        else:
            next_children = g.constructTree()
            for x in next_children:
                if (x not in nodes) or (x not in visited):
                    nodes.append(x)
    return None

def printPathStates(statePath):

    path = [statePath]
    while statePath.parent:
        statePath = statePath.parent
        path.append(statePath)
    print("\t\t\t" + "Left Side" + "\t\t\t" + "Right Side" + "\t\t" + "Boat ")
    print("\n\t Cannibals" + "\tMissionaries" + "\t\t" + "Cannibals" + "\tMissionaries" + "\tBoat Position")
    counter = 0
    for p in reversed(path):
        print("State " + str(counter) + "  Left C: " + str(p.data["left"].cannibals) + "\tLeft M: " + str(
            p.data["left"].missionaries) + "\t|\tRight C: " + str(
            p.data["right"].cannibals) + "\tRight M: " + str(p.data["right"].missionaries) + "\t| Boat: " + str(
            p.data["boat"]))
        counter = counter + 1

if __name__ == "__main__":
    solution = bfs()
    printPathStates(solution)