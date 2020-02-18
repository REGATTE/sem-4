# k size array
sizes = list(map(int, input("Enter Space Seperated k Weights : ").split(" ")))
amt = int(input("Enter Total Weight: "))

# while(amt):
#     if (amt)

minT = 999999
for sizeInd in range(len(sizes)):

    abdiv =  amt % sizes[sizeInd]
    if (abdiv == 0 and abdiv < minT and sizes[sizeInd] != 1):
        if (sizes[sizeInd]<minT):
            minT = sizes[sizeInd]

# if (absol != 999999):



print(minT)
