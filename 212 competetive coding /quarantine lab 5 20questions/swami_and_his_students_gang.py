def negProdSubArr(arr, n): 
    positive = 1
    negative = 0
    for i in range(n): 
  
        if (arr[i] > 0): 
            arr[i] = 1
        else: 
            arr[i] = -1
  
        if (i > 0): 
            arr[i] *= arr[i - 1] 

        if (arr[i] == 1): 
            positive += 1
        else: 
            negative += 1

    return (positive * negative) 
  
n=int(input())
arr =list(map(int,input().split()))
n = len(arr) 
  
print(negProdSubArr(arr, n))
