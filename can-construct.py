def solution(target, wordBank, memo = {}):
    if (target in memo):
        return memo[target]
    if (target == ""):
        return True
    for word in wordBank:
        if (target.startswith(word)):
            suffix = target[len(word):]
            if (solution(suffix, wordBank) == True):
                memo[target] = True
                return True
    memo[target] = False
    return False

if __name__ == "__main__":
    print(solution("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(solution("eeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))