inputStr = "abacadabra"
num_vowels = 0
# your code here
size = len(inputStr)
i = 0

while i < size:
    compare = inputStr[i]
    i += 1
    if compare == "a" or compare == "e" or compare == "i" or compare == "o" or compare == "u":
        num_vowels = num_vowels + 1

print(num_vowels)