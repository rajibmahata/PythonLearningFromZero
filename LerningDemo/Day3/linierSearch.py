# linier search
def linier_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [ 2, 3, 4, 10, 40 ]
x = 100
result = linier_search(arr, x)
print(f"Element is present at index {result}" if result != -1 else "Element is not present in array")