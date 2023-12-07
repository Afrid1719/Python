def solution(target, wordBank, memo = {}):
    if (target in memo):
        return memo[target]
    if (target == ""):
        return 1
    c = 0
    for word in wordBank:
        if (target.startswith(word)):
            suffix = target[len(word):]
            c += solution(suffix, wordBank, memo)
    memo[target] = c
    return c

if __name__ == "__main__":
    print(solution("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(solution("eeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))