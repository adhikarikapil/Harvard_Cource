def binarySearch(arr, low, high, number):

    # Check the base case
    if high >= low:
        mid = (high + low) // 2

        # If the number is present at the exact middle itself
        if arr[mid] == number:
            return mid

        # If the number is smaller than the middle number then it can only be present at the left side of the array
        elif arr[mid] > number:
            return binarySearch(arr, low, mid-1, number)
        # If the number is bigger than the middle number then it can only be persent at the right side of the array
        else:
            return binarySearch(arr, mid+1, high, number)

    else:

        # If not present in the array
        return -1


# Test array
arr = [2, 3, 4, 10, 40]
number = 10

# Function call
result = binarySearch(arr, 0, len(arr)-1, number)

if result != -1:
    print("The element is present at ", str(result), "index")

else:
    print("The element is not present at the array.")
