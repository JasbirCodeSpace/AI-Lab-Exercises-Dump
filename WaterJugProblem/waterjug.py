#import libraries
from collections import defaultdict

#global variables
A, B, X = 0, 0, 0
visited = defaultdict(lambda: False)

def solve(volume1, volume2):
    
    if (volume1 == X and volume2 == 0) or (volume1 == 0 and volume2 == X):
        print([volume1, volume2])
        return True
    
    if visited[(volume1, volume2)] == False:
        print([volume1, volume2])
        
        visited[(volume1, volume2)] = True

        return (solve(0, volume2) or 
                solve(volume1, 0) or 
                solve(volume1, B) or 
                solve(A, volume2) or 
                solve(volume1 - min(volume1, B - volume2), volume2 + min(volume1, B - volume2)) or 
                solve(volume1 + min(volume2, A - volume1), volume2 - min(volume2, A - volume1)))

    else:
        return False

if __name__ == "__main__":
    A = int(input("Enter the volume of jug A: "))
    B = int(input("Enter the volume of jug B: "))
    print("** NOTE: X should be strictly less than A (X < A)")
    X = int(input("Enter the desired volume: "))
    solve(A, B)