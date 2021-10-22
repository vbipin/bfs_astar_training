#In this file we keep the BFS/DFS and Greedy/A* algorithms and other useful functions

#I will try to use the minimum required libs from python
#Also the code is written with simplicity in mind than efficiency
#the code is suboptimal; to be used only as a teaching resource

#XXX
#These functions assume successors() and heuristic()
#When using you may set like this

#import solutions
#solutions.successors = successors
#solutions.heuristic  = heuristic #if using greedy or astar
# where the successors and heuristic funtions defined locally 

#########################################################################


#To find the path from start to goal from the parent dictionary
#The parents dict has the format like { node: parent, .... start : None, ...}
#By following the back pointers up the parents chain we can reach start and thus extracting the path
def get_path(parents_dict, end):  
    """returns path from start to end. start is the one with parent as None"""
    path = []
    while end is not None :
        path.append( end )
        end = parents_dict[end]
        
    return list(reversed(path)) #we were building path from end to start, so reverse it


#########################################################################
#  BFS
#########################################################################

#this is the bfs with goal check while doing the expansion

def bfs(start, goal) :
    """returns the path list of nodes from start to goal"""
    
    store   = [ start ]
    visited = { start: True } #dont care about order
    parents = { start: None } #we keep the back pointers here
    
    if start == goal :      
        return get_path(parents, goal)
    
    while store :
        #print ("-----------")
        #print ("visited:", visited)
        #print ("store:", store)
        
        current = store.pop(0) #pop(0) makes it bfs, pop() makes this dfs
        
        #print("pop:", current)
        
        for s in successors( current ) :
            if s not in visited: 
                parents[s] = current   #we set the parent pointer
                if s == goal :
                    print ("visited:", len(visited), len(parents))
                    return get_path(parents, goal)
                
                visited[s] = True      #mark the node as visited
                store.append( s )      #add the kid node to be explored later
                
                
        #print ("visited:", visited)
        #print ("store:", store)
        #print ("-----------")
    print ("visited:", len(visited), len(parents))                        
    return [] #didnt find a path


#########################################################################
#this is the bfs with goal check before expansion. This version will touch more nodes

def bfs2(start, goal) :
    """returns the path list of nodes from start to goal"""
    
    store   = [ start ]
    visited = { start: True } #dont care about order
    parents = { start: None } #we keep the back pointers here
    
    while store :
        #print ("-----------")
        #print ("visited:", visited)
        #print ("store:", store)
        
        current = store.pop(0) #pop(0) makes it bfs, pop() makes this dfs
        if current == goal :
            print ("visited:", len(visited), len(parents))
            return get_path(parents, goal)
        
        #print("pop:", current)
        
        for s in successors( current ) :
            if s not in visited: 
                parents[s] = current   #we set the parent pointer               
                visited[s] = True      #mark the node as visited
                store.append( s )      #add the kid node to be explored later
                
                
        #print ("visited:", visited)
        #print ("store:", store)
        #print ("-----------")
    print ("visited:", len(visited), len(parents))                       
    return [] #didnt find a path



#########################################################################
#  DFS
#########################################################################

#In this version of dfs we just change pop(0) to pop() to make the store a stack
#Other wise the code is identical to BFS

def dfs(start, goal) :
    """returns the path list of nodes from start to goal"""
    
    store   = [ start ]
    visited = { start: True } #dont care about order
    parents = { start: None } #we keep the back pointers here
    
    if start == goal :      
        return get_path(parents, goal)
    
    while store :
        #print ("-----------")
        #print ("visited:", visited)
        #print ("store:", store)
        
        current = store.pop() #pop(0) makes it bfs, pop() makes this dfs
        
        #print("pop:", current)
        
        for s in successors( current ) :
            if s not in visited: 
                parents[s] = current   #we set the parent pointer
                if s == goal :
                    print ("visited:", len(visited), len(parents))
                    return get_path(parents, goal)
                
                visited[s] = True      #mark the node as visited
                store.append( s )      #add the kid node to be explored later
                
                
        #print ("visited:", visited)
        #print ("store:", store)
        #print ("-----------")
    print ("visited:", len(visited), len(parents))                        
    return [] #didnt find a path

#########################################################################

def dfs2(start, goal) :
    """returns the path list of nodes from start to goal"""
    
    store   = [ start ]
    visited = { start: True } #dont care about order
    parents = { start: None } #we keep the back pointers here
    
    while store :
        #print ("-----------")
        #print ("visited:", visited)
        #print ("store:", store)
        
        current = store.pop() #pop(0) makes it bfs, pop() makes this dfs
        if current == goal :
            print ("visited:", len(visited), len(parents))
            return get_path(parents, goal)
        
        #print("pop:", current)
        
        for s in successors( current ) :
            if s not in visited: 
                parents[s] = current   #we set the parent pointer               
                visited[s] = True      #mark the node as visited
                store.append( s )      #add the kid node to be explored later
                
                
        #print ("visited:", visited)
        #print ("store:", store)
        #print ("-----------")
    print ("visited:", len(visited), len(parents))                       
    return [] #didnt find a path



#########################################################################
#  Greedy and A*
#########################################################################

#we need a priority queue for greedy and A*
#XXX This is a VERY BAD Priority Queue. 
#We use it just for debugging.

def priority_queue() :
    return {} #we use a dict as priority queue

#it returns the min number item
def priority_append(pq, item, priority) :
    pq[item] = priority #pq is just a dict
    
def priority_pop(pq) :
    min_priority = min(pq.values())
    for key in pq :
        if pq[key] == min_priority :
            pq.pop(key) #delete that item from queue
            return key, min_priority
    return None #impossible

#########################################################################

def greedy(start, goal) :
    """returns a set of nodes from start to goal. Greedy is suboptimal"""
    
    store   = priority_queue() #store is a priority queue now
    priority_append(store, start, heuristic(start,goal))
    
    visited = { start: True }
    parents = { start: None } #we keep the bak pointers here
    
    while store :
        
        current, priority = priority_pop(store) 
        
        if current == goal :
            print ("visited:", len(visited))
            return get_path(parents, goal)
        
        #This must be here. Cannot be in the expansion time because of heuristics
        visited[current] = True
        
        for s in successors( current ) :
            if s not in visited : 
                #we need a check here              
                priority = heuristic(s, goal)
                if s not in store or priority < store[s]:                   
                    priority_append(store, s, priority )
                    parents[s] = current

    #print ("visited:", len(visited))           
    return []


#########################################################################
def astar(start, goal) :
    """returns a set of nodes from start to goal"""
    
    store   = priority_queue() #store is a priority queue now
    priority_append(store, start, 0+heuristic(start,goal)) #priority value has depth + heuristic
    
    visited = { start: True }
    parents = { start: None } #we keep the bak pointers here
    
    while store :
        
        current, priority = priority_pop(store) 
        depth             = priority - heuristic(current, goal) #parent depth
        
        if current == goal :
            print ("visited:", len(visited))
            return get_path(parents, goal)
        
        #This must be here. Cannot be in the expansion time because of heuristics
        visited[current] = True
        
        for s in successors( current ) :
            if s not in visited : 
                #we need a check here              
                priority = depth + 1 + heuristic(s, goal)
                if s not in store or priority < store[s]:                   
                    priority_append(store, s, priority )
                    parents[s] = current

    #print ("visited:", len(visited))           
    return []

#########################################################################