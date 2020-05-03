# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

s = " codewars  is  nice  "
s = s.title()
s_word = [item.strip() for item in s.split()]
final = ""

for item in s_word:
    final += item

final = "#" + final

if len(final) > 140 or final == "#":
    print("False")
else:
    print(final)