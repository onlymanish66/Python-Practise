def rotateLeft(d, arr):
    # Write your code here
    newarray = []
    newarray = arr[d:] + arr[:d]
    return newarray