"""

Ex1 Bennett students have direct blessings from Goddess Athena


Bennett University CSE 2nd year has N students ordered based on their enrol numbers. Each of these students are represented by their initials in lower case alphabet as R = [r1,r2,r3…rN]. A student gang can be formed based on the adjacent students from R. A mysterious theory in academia says that a student gang is blessed directly by the Greek lord of knowledge Goddess Athena if their names have same initials. Prof. Swami who takes a fantastic course called Competitive Programming to them, is now wondering that what is the count C of such blessed student gangs in the class. If R = [abba] then C = 5 as the possible student gangs are [a], [b], [b], [a], [bb]. If R = [bbbcbb] then C = 10.

Input Format

abba

Constraints

NA

Output Format

5

Sample Input 0

abba
Sample Output 0

5

"""

R = input()+"0"

count,start = 0,0

for r in range(1,len(R)):
    if(R[start]!=R[r]):
        count+=((r-start)*(r-start+1)/2)
        start = r
        
print(int(count))