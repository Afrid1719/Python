#Product of Array Except Self

def solution(nums):
    res = [1] * len(nums)
    temp = 1
    for i in range(len(nums)):
        res[i] = temp
        temp *= nums[i]
    temp = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] *= temp
        temp *= nums[i]
    return res

if __name__ == "__main__":
    print(solution([1,2,3,4]))