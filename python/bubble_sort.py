def bubbleSort(arr):
    n = len(arr)
   
    #To iterate through every element of array 
    for i in range(n-1):
        swapped = False
        
        #To compare the adjacent elements of the array
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                #For swapping
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
        #If there is no swap required         
        if not swapped:
            return


arr = [3, 5, 4, 2, 6 ,8, 7, 9, 1]

bubbleSort(arr)
print("Sorted array is: ")


for i in range(len(arr)):
    print("% d"% arr[i], end = " ")