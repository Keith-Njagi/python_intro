# Conditional operators
# > , <, ==, !=,

# Logical operators
# or - Atleast one of the conditions have to be True
# and - All condtions have to be True to return True
# not - Basically, if the condition is false it returns True

# control structures
# if, if-else, if-elif, if-elif-else, while, for, is

n1 = 11
n2 = 12
if not n1 == n2:
    print('Eq')

if 1 == 1.0:
    print("True")
else:
    print("False")

print(1 is 1.0)
print(1/2 is 0.5)

x = 1
if 1.0 == x:
    print("Too True")
else:
    print("Lie")