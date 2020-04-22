"""
Ex1 Brahmanandam makes a Chocolate deal with his Daughter

Brahmanandam comes home and finds his daughter playing with dolls. His daughter asked him to bring pack of chocolates. Brahmanandam brought chocolates but gives his daughter a challenge to solve. He found that his daughter playing with N dolls each of them is written a lower-case alphabet on it. The alphabets written on them forms a string S (for example “abacd”). Now Brahmanandam writes one more word consisting N characters (string T). Now his daughter has to convert the S into T. Now the rules are, 1. She cannot change the sequence of the dolls, 2. She can rewrite dolls with same characters into different character (i.e. replacing all characters “c” with another character “d”). Brahmanandam finally tells his daughter that she has to tell Yes if it is possible to convert S into T, otherwise she has to tell No. If his daughter tells the wrong answer, Brahmanandam will not give the chocolates to her daughter but will eat everything by himself. Check if one string can be converted to another For example, if S = “abbcaa”; T = “bccdbb” then Output is Yes. As we can replace all ‘c’ with ‘d’, ‘b’ with ‘c’ and ‘a’ with ‘b’. If S = “abbc” and T = “bcca” then output is No.

Input Format

abbcaa bccdbb

Constraints

NA

Output Format

Yes

Sample Input 0

abbcaa
bccdbb
Sample Output 0

Yes
"""

A=[char for char in str(input())]
B=[char for char in str(input())]
for i in range(len(A)):
    if(A[i]!=B[i]):
        B=[A[i] if X==B[i] else X for X in B]
if(A==B):
    print('Yes')
else:
    print('No')