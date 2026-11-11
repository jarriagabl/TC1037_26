# When using a for-loop,
# changes to `value` won't
# modify the corresponding
# list elements
values = [2, 4, 6]
for value in values:
    value *= 2 # Shortcut for value = value * 2
    print(value)
print(values) # Prints [2, 4, 6]

# Using a while-loop will
# allow us to modify list
# elements through index
# notation (lst[index] = ... )
i = 0
while i < len(values):
    values[i] *= 2
    print(values[i])
    i += 1
print(values) # Prints [4, 8, 12]