s1 = [5, 10, 7, 1, 3]
buffer = []
target = []

min_val = s1.pop()

while len(s1) > 0 or len(buffer) > 0:
    if len(s1) > 0:
        val = s1.pop()
        if min_val > val:
            buffer.append(min_val)
            min_val = val
        else:
            buffer.append(val)

    if len(s1) == 0:
        target.append(min_val)
        while len(buffer) > 0:
            s1.append(buffer.pop())
    if len(s1) > 0 and len(buffer) == 0:
        # reset min
        min_val = s1.pop()
        if len(s1) == 0:
            target.append(min_val)


print(target)
print(s1)

