array = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]

arrayd = []
i = 0

while i <= len(array) - 1:
    if array[i] == 0 and array[i] is not False:
        arrayd.append(array.pop(i))
        i = i - 1
    i += 1

array = array + arrayd
print(array)