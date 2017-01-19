#! /usr/bin/python3
from heapq import heappush, heappop, heapify
import queue
class Graph(object):
        
    #initialises class
    def __init__(self):
                                 
        #vertices
        self.nodes = dict()
        #this will have dist between two points
        self.dist = dict()
        self.dfsvisited = dict()
        self.bfsvisited = dict()
        return None

    #inserts point into graph
    def insert(self, vertice):
        
        points = []
        if(self.nodes.get(vertice) == None):
            self.nodes[vertice] = points        
            self.dist[vertice] = {}
            self.dfsvisited[vertice] = False
            self.bfsvisited[vertice] = False
        return None
        
    #connects vertice2 to vertice1 and vice versa
    def connect(self, vertice1,vertice2, distance):
       
        points1 = None
        points2 = None
        #checks if either vertices are empty
        if(self.nodes.get(vertice1) == None):
            self.dist[vertice1] = {}
            points1 = []
            
        else :
            points1 = self.nodes[vertice1]
            
    
        if(self.nodes.get(vertice2) == None):
            points2 = []
            self.dist[vertice2] = {}
            
        else:
            points2 = self.nodes[vertice2]        
                
        points1.append(vertice2)
        points2.append(vertice1)
        self.dist[vertice1][vertice2] =  distance
        self.dist[vertice2][vertice1] = distance
        self.nodes[vertice1] = points1
        self.nodes[vertice2] = points2
        return 0

    def disconnect(self,source,vertice):
        adj = self.nodes[source]
        adj = adj.remove(vertice)
        self.nodes[source] = adj
        return 0
        
    def get_neighbours(self, vertice):
        if(vertice != None and self.nodes.get(vertice) != None):
            return self.nodes[vertice]
        else :
            print("Not a valid vertice")
            return None
    
    def remove(self,vertice):
        if(self.nodes.get(vertice) == None):
            print("Not valid node")
        else :
            
            del self.nodes[vertice]
            del self.dist[vertice]
            for key in self.dist:
                (self.dist[key]).pop(vertice, None)
                    
                        
        return None



    
    #uses djikstra's shortest path algorithm
    #returns the distances and vertices traversed for each vertice
    def shortest_path(self, graph, source):    
        distTo = dict()
        pathTo = dict()
        for key in graph.nodes:
            dist_to[key] = float("inf")
        dist_to[source] = 0
        pqueue = []
        heappush(pqueue,[source,0.0])
        
        while (len(pqueue) > 0 ):
            vertice = heappop(pqueue)
            for v in graph.nodes[vertice[0]]:
                route= []
                print(v)
                self.relax(dist_to,pqueue,vertice[0],v,path_to,graph)
                graph.get_dist(vertice[0],v,graph)
        result = {}
        for key in path_to:
            result[key] = [dist_to[key],path_to[key]]
        return result
    
	#gets
    def get_dist(self, vertice1, vertice2,graph):
        return self.dist[vertice1][vertice2]

	#relaxes an edge and determines if current path is
	#shorter than previous shortest path to vertice
    def relax(self, dist_to, pq,vertice1,vertice2,path_to,graph):
        weight = graph.dist[vertice1][vertice2]
        currentDist = weight +  dist_to[vertice1]
        if(dist_to[vertice2] > currentDist):
            dist_to[vertice2] = currentDist
            path_to[vertice2] = vertice1
            for i in  pq:
                
                if(vertice2 in i[0]):
                    i[1] = dist_to[vertice2]
                    heapify(pq)
                    return 1
                    
            heappush(pq,[vertice2,dist_to[vertice2]])
            return 1
        else:
            return 0

    def depth_first_search(self,graph,vertex):
        graph.dfsvisited[vertex] = True
        for node in graph.nodes[vertex]:
            if(graph.dfsvisited[node] != True):
                graph.depth_first_search(graph,node)
   
   
    def bfs(self,graph,vertex):
        graph.bfsvisited[vertex] = True
        q = Queue()
        q.put(vertex)         
        item = q.get()
        while(item is not None):
            for node in graph.nodes[item]:
                if(graph.bfsvisited[node] == False):
                   q.put(node)
                   self.bfsvisited[vertex] = True
            
      
    def dfs_is_visited(self, vertex):
	    return self.dfsvisited[vertex] 
           
    def print_keys(self):

        for key in self.nodes:
            print("%s\n" % str(key))
        return 0

    pass

