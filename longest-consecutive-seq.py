import time

def solution(nums):
    numsSet = set(nums)
    longest = 0
    for n in numsSet:
        if (n - 1) not in numsSet:
            length = 0
            while (n + length) in numsSet:
                length += 1
            longest = max(length, longest)
    return longest

if __name__ == "__main__":
    print(solution([100,4,200,1,2,3]))
    print(solution([100,4,200,1,2,3,25,10,11,12,3,13,14,15,16]))
    print(solution([10,9,8,7,6,5,4,3,2,1,0]))