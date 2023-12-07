import math

def solution(arr, n):
    return binarySearch(arr, n, 0, len(arr) - 1)

def binarySearch(arr, n, l, r):
    mid = l + math.trunc((r - l)/2)
    if l > r:
        return mid
    if (arr[mid] == n):
        return mid
    if (arr[mid] < n):
        return binarySearch(arr, n, mid + 1, r)
    return binarySearch(arr, n, l, mid - 1)

if __name__ == "__main__":
    print(solution([1,3,5,6], 0))
    print(solution([1,3,5,6], 4))
    print(solution([1,3,5,6], 7))
    print(solution([1,3,5,6,9], 7))
    print(solution([7,7,7,7], 7))