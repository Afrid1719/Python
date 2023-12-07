def solution(strs):
    anagrams = {}
    for s in strs:
        hashed = hash_str(s)
        if hashed in anagrams:
            anagrams[hashed] += [s]
        else:
            anagrams[hashed] = [s]
    return [anagrams[x] for x in anagrams]

def hash_str(str):
    sortedStr = "".join(sorted(list(str)))
    return sortedStr

if __name__ == "__main__":
    print(solution(["eat","tea","tan","ate","nat","bat"]))
    print(solution(["a"]))
    print(solution([""]))