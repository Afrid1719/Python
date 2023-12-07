def solution(nums, target, memo = {}):
    if (target in memo): return memo[target]
    if (target == 0): return []
    if (target < 0): return None
    shortestCombination = None
    for val in nums:
        res = solution(nums, target - val, memo)
        if (res is not None):
            combination = [val] + res
            if (shortestCombination is None or (len(combination) < len(shortestCombination))):
                shortestCombination = combination
    memo[target] = shortestCombination
    return memo[target]

if __name__ == "__main__":
    print(solution([2,3,5], 8))
    print(solution([1,4,25], 100))