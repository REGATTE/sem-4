n,m = map(int,input().split())
from math import sqrt, floor 
def minOperations( n, m) : 
    a = 0; k = 1; 
    p = max(n, m); 
    while (n != m) : 
        s = float(p - n + p - m); 
        q = (-1 + sqrt(8 * s + 1)) / 2; 
        if (q - floor(q) == 0) : 
            a = q; 
            n = m; 
        p = p + 1; 
    return a; 
if _ name _ == "_ main _" : 
    print(int(minOperations(n, m)));
