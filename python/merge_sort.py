#Funtion for merging the left and right side of the array
def merge(array, left, mid, right):
    
    n1 = mid - left + 1
    n2 = right - mid
  
    #Create temp array
    L = [0] * (n1)
    R = [0] * (n2)
    
    #Copying the data to the temp array
    for i in range(n1):
        L[i] = array[left + i]
    
    for j in range(n2):
        R[j] = array[mid + 1 + j]
        
    #Merging the temp array back
    i = 0
    j = 0
    k = left
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
            
        else:
            array[k] = R[j]
            j += 1
        k += 1
        
    #Copy the remaining element of L[]
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    
    #Copy the remaining element of R[]
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1
    
#left is for left index
#right is for right index
#array is to be sorted
def mergeSort(array, left, right):
    if left < right:
        
        mid = left + (right - left) // 2
       
        #Sort left half of the array 
        mergeSort(array, left, mid)
        
        #Sort right half of the array
        mergeSort(array, mid + 1, right)
        
        #Merge these halves of the array 
        merge(array, left, mid, right)
    else:
        return 0;   

def printArray(array, size):
    for i in range(size):
        print("% d"%array[i], end=" ")
        
        
#Driver Code
array = [7, 2, 5, 4, 1, 6, 0, 3]
size = len(array);

#Print the given array using funtion
print("Given array is: ") 
printArray(array, size)

#Sort the given array
mergeSort(array, 0, size-1)        

#Display the sorted array
print("\n")
printArray(array,size)