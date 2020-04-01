houses.sort()
    i = 0
    while i < noofhouses and budget >= houses[i]:
        budget -= houses[i]
        i += 1
    return i
