/*

Ravindra Jadeja is a naughty CSE student in Bennett University. Jadeja one day he tried to peek into his roommate Rohit Sharma’s suitcase. The suitcase has security system with 4-digit numbers. When Jadeja was trying to open the suitcase, Rohit catches him. Jadeja then smiles like an innocent boy. Now Rohit says that Jadeja will allow him to have a look inside the suitcase if he can do the unlocking in the following way. Rohit will reveal the actual pin Y (prime number) and set the lock with 4 digit prime number X. Now Jadeja has to change only one digit of X at a time. The number he sets from X should be a prime number. Then one digit of that prime number can be changed where the next number should also be a prime number. In this way Jadeja has to change X into Y by changing one digit at a time where each number on the series should be a prime number. Since Jadeja is a lazy boy he was wondering that what is the minimum number of times Z he can do the iteration to convert a prime number X to prime number Y. 
If suppose X = 1033 and Y = 8179, then sequence is 1033, 1733, 3733, 3739, 3779, 8779, 8179. So the answer Z = 6. Similarly if X = 1373 and Y = 8017 then Z=7. If X=1033 and Y = 1033 then Z=0.

Input Format

1033 8179

Constraints

NA

Output Format

6

Sample Input 0

1033 8179
Sample Output 0

6
*/

import queue  
  
class Graph:  
      
    def __init__(self, V): 
        self.V = V;  
        self.l = [[] for i in range(V)] 
          
    def addedge(self, V1, V2): 
        self.l[V1].append(V2);  
        self.l[V2].append(V1); 
  
    # in1 and in2 are two vertices of graph   
    # which are actually indexes in pset[]  
    def bfs(self, in1, in2): 
        visited = [0] * self.V 
        que = queue.Queue() 
        visited[in1] = 1
        que.put(in1) 
        while (not que.empty()):  
            p = que.queue[0]  
            que.get() 
            i = 0
            while i < len(self.l[p]): 
                if (not visited[self.l[p][i]]): 
                    visited[self.l[p][i]] = visited[p] + 1
                    que.put(self.l[p][i]) 
                if (self.l[p][i] == in2): 
                    return visited[self.l[p][i]] - 1
                i += 1
      
    # Returns true if num1 and num2  
    # differ by single digit. 
      
# Finding all 4 digit prime numbers  
def SieveOfEratosthenes(v): 
      
    # Create a boolean array "prime[0..n]" and   
    # initialize all entries it as true. A value  
    # in prime[i] will finally be false if i is  
    # Not a prime, else true.  
    n = 9999
    prime = [True] * (n + 1) 
  
    p = 2
    while p * p <= n: 
  
        # If prime[p] is not changed,  
        # then it is a prime  
        if (prime[p] == True): 
  
            # Update all multiples of p 
            for i in range(p * p, n + 1, p): 
                prime[i] = False
        p += 1
  
    # Forming a vector of prime numbers 
    for p in range(1000, n + 1): 
        if (prime[p]):  
            v.append(p) 
      
def compare(num1, num2): 
      
    # To compare the digits  
    s1 = str(num1)  
    s2 = str(num2) 
    c = 0
    if (s1[0] != s2[0]): 
        c += 1
    if (s1[1] != s2[1]): 
        c += 1
    if (s1[2] != s2[2]): 
        c += 1
    if (s1[3] != s2[3]):  
        c += 1
  
    # If the numbers differ only by a single  
    # digit return true else false  
    return (c == 1) 
      
def shortestPath(num1, num2): 
      
    # Generate all 4 digit  
    pset = []  
    SieveOfEratosthenes(pset)  
  
    # Create a graph where node numbers  
    # are indexes in pset[] and there is  
    # an edge between two nodes only if  
    # they differ by single digit.  
    g = Graph(len(pset)) 
    for i in range(len(pset)): 
        for j in range(i + 1, len(pset)): 
            if (compare(pset[i], pset[j])):  
                g.addedge(i, j)      
  
    # Since graph nodes represent indexes  
    # of numbers in pset[], we find indexes 
    # of num1 and num2.  
    in1, in2 = None, None
    for j in range(len(pset)): 
        if (pset[j] == num1): 
            in1 = j 
    for j in range(len(pset)): 
        if (pset[j] == num2):  
            in2 = j 
  
    return g.bfs(in1, in2) 

num1, num2 = input().split()
num1, num2 = int(num1), int(num2)
print(shortestPath(num1, num2)) 