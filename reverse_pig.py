import string
pig_it = 'Pig latin is cool !'  # igPay atinlay siay oolcay !
#Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

words = pig_it.split()
str1 = ""

for word in words:
    if word not in string.punctuation:
        wordlist = list(word)
        size = len(wordlist) - 1
        wordlist.insert(size, wordlist.pop(0))
        wordlist.append("a")
        wordlist.append("y")
        str1 = str1 + " " + "".join(wordlist)
    else:
        str1 = str1 + " " + word

str2 = str1[1:]
print(str2)