def collatzSequenceLen(k):
    if k == 0:
        return 0
    if k == 1:
        return 1
    elif k % 2 == 0:
        return 1+collatzSequenceLen(k/2)
    return 1+collatzSequenceLen(3*k+1)

print collatzSequenceLen(3)
print collatzSequenceLen(4)
print collatzSequenceLen(5)