import math

in_matrix = [
    [0, -1, 1,1,-1,1],
    [1, 0, 1,-1,1,1],
    [1, -1, 0,1,-1,-1],
    [-1,1,1,0,-1,-1],
    [1,1,1,-1,0,-1],
    [1,-1,-1,1,1,0]
]

frequency_table={}
for i in range(len(in_matrix)):
    frequency_table[i] = {
        'correct':0,
        'fault':0
    }

for r_index in range(len(in_matrix)):
    for d_index in range(len(in_matrix[r_index])):
        if (d_index!=r_index):
            if(in_matrix[r_index][d_index]==-1):
                frequency_table[d_index]['fault']+=1
            elif(in_matrix[r_index][d_index]==1):
                frequency_table[d_index]['correct']+=1

consensus_cnt = math.floor(len(in_matrix)/2)



for key in frequency_table:
    if (frequency_table[key]['correct'] >= consensus_cnt):
        print(f"{key} is functioning correctly")

sum=0
for j in range(6):
  for i in range(len(in_matrix)):
    sum+=in_matrix[i][j]
  print(sum)

