# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000
#
# test.describe("Example Tests")
# test.assert_equals(solution('XXI'), 21, 'XXI should == 21')
# test.assert_equals(solution('I'), 1, 'I should == 1')
# test.assert_equals(solution('IV'), 4, 'IV should == 4')
# test.assert_equals(solution('MMVIII'), 2008, 'MMVIII should == 2008')
# test.assert_equals(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')

roman = "IV"
di = {'I': 1, 'V': 5, 'VI': 6, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# signToValue = [di[c] for c in roman]
decode = []
for c in roman:
    decode.append(di[c])

x = 0
actual = 0

for item in decode[::-1]:
    print(item)
    if item >= actual:
        x += item
    else:
        x -= item
    actual = item

print(x)