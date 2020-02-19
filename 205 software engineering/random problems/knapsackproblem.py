items =[
["A",24,12,"complete"],
["B",13,7,"complete"],
["C",23,11,"complete"],
["D",15,8,"complete"],
["E",16,9,"complete"],
["F",15,3,"complete"]]
sum = 0
size = 14
profit = 0
new = sorted(items,key=lambda x: x[1],reverse = True)
final =[]
# new.sort(reverse = True)
for i in range(0,len(items)):
  while(sum<size):
    final.append(new[i])
    sum +=new[i][2]
    profit += new[i][1]
    new.remove(new[i])
    if(sum>size):
      sum = size
      final[len(final)-1][3]='partial'
print("\n")
for i in range(len(final)):
  print(final[i])
print("\n")
print(profit)
print("\n")

print(sum)
