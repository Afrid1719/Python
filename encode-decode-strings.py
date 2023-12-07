def encode(strArr):
    encoded = ""
    for s in strArr:
        prefix = str(len(s)) + "#"
        encoded += prefix + s
    return encoded

def decode(str):
    decoded, i = [], 0
    while i < len(str):
        n = int(str[i])
        j = i + 2
        decoded.append(str[j: n + j])
        i = n + j
    return decoded

if __name__ == "__main__":
    data = ["life", "cod4#e", "coffee", "he#r"]
    print("Original:", data)
    encoded = encode(data)
    print("Encoded: ", encoded)
    decoded = decode(encoded)
    print("Decoded: ", decoded)