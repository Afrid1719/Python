def solution(nums, target):
    hash_table = {}
    for (idx, val) in enumerate(nums):
        rem = target - val
        if val in hash_table:
            return [hash_table[val], idx]
        hash_table[rem] = idx
    return []
    
if __name__ == "__main__":
    print(solution([11,15, 7, 2], 9))
    print(solution([3,2,4], 6))
    print(solution([3,3], 6))
    print(solution([0,4,3,0], 0))