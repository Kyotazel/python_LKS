def selectionSort(items):
  for i in range(len(items)):
    minPos = i
    for j in range(i,len(items)):
      if items[j] < items[minPos]:
        minPos = j
    
    temp = items[minPos]
    items[minPos] = items[i]
    items[i] = temp
    
   
arr = [7,4,8,3,0,1,20,-100,-20,10000,50000]

selectionSort(arr)

print(arr)