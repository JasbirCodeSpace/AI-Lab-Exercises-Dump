

import sys
import random
import copy
import numpy as np

class State:
    
    def __init__(self, route:[], distance:int=0):
        self.route = route
        self.distance = distance
    
    def __eq__(self, other):
        for i in range(len(self.route)):
            if(self.route[i] != other.route[i]):
                return False
        return True
   
    def __lt__(self, other):
         return self.distance < other.distance
    
    def __repr__(self):
        return ('({0},{1})\n'.format(self.route, self.distance))
    
    def copy(self):
        return State(self.route, self.distance)
    
    def deepcopy(self):
        return State(copy.deepcopy(self.route), copy.deepcopy(self.distance))
   
    def update_distance(self, matrix, home):
        
        self.distance = 0
        
        from_index = home
       
        for i in range(len(self.route)):
            self.distance += matrix[from_index][self.route[i]]
            from_index = self.route[i]
       
        self.distance += matrix[from_index][home]

class City:
   
    def __init__(self, index:int, distance:int):
        self.index = index
        self.distance = distance
  
    def __lt__(self, other):
         return self.distance < other.distance

def probability(p):
    return p > random.uniform(0.0, 1.0)

def exp_schedule(k=20, lam=0.005, limit=1000):
    return lambda t: (k * np.exp(-lam * t) if t < limit else 0)




def get_best_solution_by_distance(matrix:[], home:int):
    
    route = []
    from_index = home
    length = len(matrix) - 1
    
    while len(route) < length:
         
        row = matrix[from_index]
       
        cities = {}
        for i in range(len(row)):
            cities[i] = City(i, row[i])
       
        del cities[home]
        for i in route:
            del cities[i]
       
        sorted = list(cities.values())
        sorted.sort()
        
        from_index = sorted[0].index
        route.append(from_index)
    
    state = State(route)
    state.update_distance(matrix, home)
   
    return state


def mutate(matrix:[], home:int, state:State, mutation_rate:float=0.01):
  
    mutated_state = state.deepcopy()

    for i in range(len(mutated_state.route)):
  
        if(random.random() < mutation_rate):
          
            j = int(random.random() * len(state.route))
            city_1 = mutated_state.route[i]
            city_2 = mutated_state.route[j]
            mutated_state.route[i] = city_2
            mutated_state.route[j] = city_1
  
    mutated_state.update_distance(matrix, home)

    return mutated_state

def simulated_annealing(matrix:[], home:int, initial_state:State, mutation_rate:float=0.01, schedule=exp_schedule()):

    best_state = initial_state
   
    for t in range(sys.maxsize):
      
        T = schedule(t)
      
        if T == 0:
            return best_state
       
        neighbor = mutate(matrix, home, best_state, mutation_rate)
  
        delta_e = best_state.distance - neighbor.distance
    
        if delta_e > 0 or probability(np.exp(delta_e / T)):
            best_state = neighbor

def main():
 
    cities=['DELHI','BHOPAL','KOLKATA','KANPUR','RANCHI','LUCKNOW']
    city_indexes = [0,1,2,3,4,5]
 
    
  
    print(cities)
    v=int(input("Enter number of vertices :"))
    # Distances in miles between cities, same indexes (i, j) as in the cities array
    
    
    matrix=[[0 for  x in range(v)]  for y in range(v)]
    
    for i in range(v):
        for j in range(v):
            matrix[i][j]=int(input(f'distance from {cities[i]} -> {cities[j]}:'))
   
    home = int(input("enter city index (0 based indexing):"))
    # Get the best route by distance
    
    state = get_best_solution_by_distance(matrix, home)
    
    print('\n-- Best solution by distance --')
    
    print(cities[home], end='')
    
    for i in range(0, len(state.route)):
       print(' -> ' + cities[state.route[i]], end='')
    
    print(' -> ' + cities[home], end='')
    
    print('\n\nTotal distance: {0} miles'.format(state.distance))
    
    print()
   

    # Run simulated annealing to find a better solution
    state = get_best_solution_by_distance(matrix, home)
    
    
    state = simulated_annealing(matrix, home, state, 0.1)
    print('\n-- Simulated annealing solution --')
    print(cities[home], end='')
    for i in range(0, len(state.route)):
       print(' -> ' + cities[state.route[i]], end='')
    print(' -> ' + cities[home], end='')
    print('\n\nTotal distance: {0} miles'.format(state.distance))
    print()


# Tell python to run main method
if __name__ == "__main__": 
    main()
    


# In[ ]:


# 0 4 10 6
# 4 0 5 11
# 10 5 0 2
# 6 11 2 0

