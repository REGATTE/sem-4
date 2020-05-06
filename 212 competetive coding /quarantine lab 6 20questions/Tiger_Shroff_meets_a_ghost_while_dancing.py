n = int(input())
def multiple(A): 
    t = False
    i = 1
    while(t != True):   
        result= A * i 
        a = set('01') 
        S = str(result) 
        if set(S).issubset(a): 
            t = True; 
            break; 
        else: 
            i = i + 1        
    return S
print(multiple(n))