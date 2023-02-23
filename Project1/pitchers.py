import math
import sys
import time

#function to get multiple GCD
def multi_gcd(array):
    l = len(array)
    if l == 1:
        return array[0]
    elif l == 2:
        return math.gcd(array[0], array[1])
    else:
        return math.gcd(multi_gcd(array[:l//2]), multi_gcd(array[l//2:]))

# I define a node class
class Node:
    capacities = []#Capacities

    def __init__(self, states, g=0, path=[]):
        self.states = states #The state of the water in the pitchers
        self.g = g #Actual cost
        self.h = self.getH() #Estimated cost  
        self.path = path #Path

    def getH(self): #My heuristic
        remain = self.capacities[-1] - self.states[-1]
        h = math.ceil(remain / max(self.capacities[:-1]))
        return h

    def getF(self): #F = H + G
        return self.h + self.g

# Defined a clss Pitchers
class Pitchers:
    # A* Alogrithm
    def Astar_Search(self,inputfile):

        fo = open(inputfile, mode='r') # Read file
        line = fo.readline() #Read a line
        if line[-1] == '\n':
            line = line[:-1]
        capacities = [ int(c) for c in line.split(',') ] #Process rows, get capacity
        line = fo.readline() # Read another line
        if line[-1] == '\n':
            line = line[:-1]
        capacities.append(int(line)) #Concatenate into a list
        fo.close()

        gcd = multi_gcd(capacities[:-1])
        if capacities[-1] % gcd > 0:
            return -1, None

        pitchnum = len(capacities)
        Node.capacities = capacities

        start_states = [0 for _ in range(pitchnum)] #Initialization, all are 0
        start_node = Node(start_states,0,[])
        close_list = set()
        close_list.add(start_states[-1])
        open_list = [start_node]

        while (open_list != []):

            current_node = open_list.pop(0)
            current_states = current_node.states
            current_g = current_node.g
            current_path = current_node.path

            # deque the answer, return
            if current_states[-1] == capacities[-1]:
                return current_g, current_node

            # pour any water pitcher into the infinite one
            for i in range(pitchnum-1):
                # if the new state is visited, just skip
                if current_states[-1] + capacities[i] in close_list:
                    continue
                new_states = current_states[:]
                new_path = current_path[:]
                if new_states[i]:
                    new_states[i] = 0
                    new_g = current_g + 1
                else:
                    new_g = current_g + 2
                    
                # calculate the new state related variables
                new_path.append(capacities[i])
                new_states[-1] = current_states[-1] + capacities[i]
                close_list.add(new_states[-1])
                open_list.append(Node(new_states,new_g,new_path))
                open_list.sort(key=lambda element:element.getF())

            # pour the infinite one into any water pitcher
            for i in range(pitchnum-1):
                # if the new state is invalid or visited, just skip
                if current_states[-1] - capacities[i] < 0:
                    continue
                if current_states[-1] - capacities[i] in close_list:
                    continue

                new_states = current_states[:]
                new_path = current_path[:]
                if new_states[i]:
                    new_g = current_g + 2
                else:
                    new_states[i] = 1
                    new_g = current_g + 1
                # calculate the new state related variables
                new_path.append(-capacities[i])
                new_states[-1] = current_states[-1] - capacities[i]
                close_list.add(new_states[-1])
                open_list.append(Node(new_states,new_g,new_path))
                open_list.sort(key=lambda element:element.getF()) #Sort by the f size of each node, the smaller the front processing

        return -1, None


def TestFile(filename):
    pitchers = Pitchers()
    start_time = time.time()
    steps, node = pitchers.Astar_Search(filename)
    end_time = time.time()
    print(f"File name: {filename}")
    print(f"Pitchers capacities: {node.capacities[:-1]}")
    print(f"Target: {node.capacities[-1]}")
    print(f"Steps: {steps}")
    if node:
        print(f"Path: {node.path}")
    else:
        print(f"Path: No Path!")
    print(f"Time cost: {format(end_time - start_time, '.3f')}s\n")

# main function
if __name__ == '__main__':

    if len(sys.argv) > 1:
        TestFile(sys.argv[1])
    else:
        test_files = ['input1.txt', 'input2.txt', 'input3.txt',
                      'input4.txt', 'input5.txt', 'input6.txt',
                      'input7.txt', 'input8.txt', 'input9.txt']
        for filename in test_files:
            TestFile(filename)
