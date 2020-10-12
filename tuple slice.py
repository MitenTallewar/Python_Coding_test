"""
Write the function to slice the tuple between the given start (inclusive) and end (exclusive) iRdexes,
and join the resulting range of values as a comma delimited string.
For example, tuple_slice(1, 4, (76, 34, 13, 64, 12) should return "34,13,64".

"""
                 #1   #4
def tuple_slice(start,end,tup):
    l = len(tup) #  5
    ans = None
    l1 = []
    for i in range(l-1): #4
        if i >= start and i <= end:
            l1.append(str(tup[i]))
            ans = ",".join(l1)
    return '"'+ ans +'"'

print(tuple_slice(1,4,(35,40,26,50,26)))

