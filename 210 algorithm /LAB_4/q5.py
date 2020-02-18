# k size array
sizes = list(map(int, input("Enter Space Seperated k Weights : ").split(" ")))
amt = int(input("Enter Total Weight: "))

amts = [0 for x in sizes]
cnt = 0
tcnt = 0
for sizeInd in range(len(sizes)):
    if (amt > sizes[sizeInd]-1):
        while (amt > sizes[sizeInd]-1):
            amts[cnt]+=1
            amt-=sizes[sizeInd]
    else:
        amts[cnt]= 0
    tcnt+=amts[cnt]
    print(f"Size {sizes[sizeInd]} Trucks : {amts[cnt]}")
    cnt+=1

print(f"\nTotal Trucks Required : {tcnt}")
