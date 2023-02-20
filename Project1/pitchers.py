import copy


open_list = []#Contained those who are ready to move but have not yet moved
close_list = []#Contained those already gone

class Node:
    capacities = []#Capacities

    def __init__(self, states, parent=[], step=0):
        self.states = states #The state of the water in the pitchers
        self.parent = parent #Transfer from which state
        self.step = step#Save steps
        if parent:
            self.SetParent(parent)
        self.H = self.GetH() #Heuristic

    def SetParent(self,parent):#It will be used later
        self.parent = parent
        self.step = parent.step + 1

    def GetH(self): #Estimated cost
        remain = self.capacities[-1] - self.states[-1] #Last digit (target goal) - the same digit but after updating the status
        hmin = remain
        for x in self.states[:-1]: #Start traversing from the list excluding the last one digit, find the minimum, try to fill the biggest one first
            h = abs(remain - x) #Remain as the most basic value, closest to target goal. 
            if h in self.capacities[:-1]:#If the remaining capacity of this part just matches the capability of the pitcher, that pitcher will be used directly regardless of the situation that is closer to the remaining.
                hmin = 0
                break
            if h < hmin:
                hmin = h
        return hmin + remain

    def GetF(self): #F= G+H
        return self.H + self.step * 2 #Step is G, the smaller the better



def PrintPath(current_node):
    best_path = []
    while(current_node):
        best_path.append(current_node.states)
        current_node = current_node.parent
    best_path.reverse()
    print("The shortest path has %d steps" % (len(best_path)-1))
    print(best_path)

def Pour_X(states,x):# Fill x
    states[x] = Node.capacities[x]

def Empty_X(states,x):# Empty X
    states[x] = 0

def Pour_X_To_Y(states,x,y): # Pour X to Y
    if (states[x] + states[y]) <= Node.capacities[y]:
        states[y] += states[x]
        states[x] = 0
    else:
        states[x] -= Node.capacities[y] - states[y]
        states[y] = Node.capacities[y]

def Empty_X_To_Virtual(states,x): # Pour all X into the virtual pitcher
    states[-1] += states[x]
    states[x] = 0

def GetStInList(nlist,states):
    for i in range(len(nlist)):
        if nlist[i].states == states:
            return i
    return -1


def UpdateList(node, states):
    if GetStInList(close_list, states) == -1:# not in close list
        pos = GetStInList(open_list, states)
        if  pos == -1:# create node
            open_list.append(Node(states,node))
        elif node.step + 1 < open_list[pos].step:# update node
            open_list[pos].SetParent(node) #The position changed a younger parent       
    
class Pitchers:#For test cases, use a class 
    def SearchPath(self,inputfile):

        fo = open(inputfile, mode='r')# Read file
        line = fo.readline()#Read a line
        if line[-1] == '\n':
            line = line[:-1]
        capacities = [ int(c) for c in line.split(',') ] #Process rows, get capacity
        line = fo.readline()# Read another line
        if line[-1] == '\n':
            line = line[:-1]
        capacities.append(int(line))# Concatenate into a list
        fo.close()
        print(capacities)

        Node.capacities = capacities
        open_list.clear()
        close_list.clear()
        open_list.append(Node([0]*len(capacities)))#Initialization, all are 0
        loop = 0
        while(open_list != []):#As long as it's not empty
            loop += 1
            current_node = open_list.pop(0)
            close_list.append(current_node)
            if(current_node.states[-1] == Node.capacities[-1]):#If the target goal is reached
##                print("Success")
##                print("Search loop %d" % loop,end=",")
                PrintPath(current_node)
                print(current_node.step)
                return current_node.step
            #add new reachable board into open_list

            current_states = current_node.states
            pitchernum = len(current_states) #Number of pitchers
            for x in range(pitchernum-1):#Exclude the virtual pitcher first, and operate other pitchers first
                if current_states[x]>0:#If x has water
                    new_states = copy.deepcopy(current_states)
                    Empty_X(new_states, x)
                    UpdateList(current_node, new_states)

                    for y in range(pitchernum-1):
                        if y == x:
                            continue
                        if current_states[y]<Node.capacities[y]:#If y is not full
                            new_states = copy.deepcopy(current_states)
                            Pour_X_To_Y(new_states,x,y)#x can pour to y
                            UpdateList(current_node, new_states)

##                        if current_states[x]<Node.capacities[x] and current_states[y]>0:
##                            new_states = copy.deepcopy(current_states)
##                            Pour_X_To_Y(new_states,y,x)
##                            UpdateList(current_node, new_states)

                    if current_states[x]+current_states[-1]<=Node.capacities[-1]: #Pour water into the virtual pitcher, but it cannot exceed the target goal
                        new_states = copy.deepcopy(current_states)
                        Empty_X_To_Virtual(new_states,x)#Empty x into the virtual pitcher
                        UpdateList(current_node, new_states)

                if current_states[x]<Node.capacities[x]:#x is out of capacity
                    new_states = copy.deepcopy(current_states)
                    Pour_X(new_states, x) # fill up x
                    UpdateList(current_node, new_states)
                    
            open_list.sort(key=lambda element : element.GetF()) #A* openlist reordering, key is the minimum cost value F
            
##        print("Fail")
##        print("Search loop%d" % loop,end=",")
        print(-1)
        return -1


if __name__ == '__main__':

    pitchers = Pitchers()
    result = pitchers.SearchPath("input6.txt")
    print( result )
