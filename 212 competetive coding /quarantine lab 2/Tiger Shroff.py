/*
Tiger Shroff one day practises dance till the midnight 12 O’clock in his studio. The ghost which lives in the studio became awake when it heard loud dance music playing in the room. Ghost then decides to capture Tiger, so it locks the building. When Tiger is done with dance, ghost stops him and says that he has to solve a puzzle to get out. Ghost says that a number is a Bingo if it has only binary digits in it for example 101, 1101, 11 etc. Now Ghost gives a number X to Tiger and asks Tiger to find the smallest Bingo number Y which can be divisible by X. Now you gotta help Tiger to go home by finding Y. For example, if X=2 then Y = 10. If X = 17 then Y = 11101

Input Format

2

Constraints

NA

Output Format

10
*/

def bin_digit(num): 
    found = False
    i = 1
    se = set('01')
    while(found != True): 
        result = num * i 
        check = str(result) 
        if(set(check).issubset(se)): 
            found = True 
            break
        else: 
            i = i + 1
            
    return check 

n = int(input())
print(bin_digit(n))