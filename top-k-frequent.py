def solution(nums, k):
    count = {}
    for n in nums:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    sortedCount = sorted(count.items(), key=lambda c: c[1], reverse=True)
    result = []
    for i in range(k):
        result.append(sortedCount[i][0])
    return result

if __name__ == "__main__":
    print(solution([1,1,1,4,5,2,2,3,5], 2))