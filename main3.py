def maxElementArray(a):

    length = len(a)

    if length == 1:
        return a [0]
    
    return max(a[0],maxElementArray(a[1:]))

a = [1,2,234,234,745,3,6,653]
print("Largest element of array: ",maxElementArray(a))