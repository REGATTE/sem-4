sizes = [25, 10, 5, 1]
amt = int(input("Enter Total Weight: "))

amts = [0 for x in sizes]
sizes.sort(reverse=True)
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
