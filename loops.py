"""

"""
#for loop
count_list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for number in count_list:
#    print(number)
    n =20

print(number)

#print a list containing a range of numbers
var_list =[]
for val in range(3,10):
    var_list.append(val)
print(var_list)

#print a list containing a range of numbers that prints each time it updates

var_list1 =[]
for val in range(3,10):
    var_list1.append(val)
    print(var_list1)
"""

DOESN'T WORK

var_list2 =[]
count1 = 0
for val in range(0,10):
    var_list2[count1].insert(val)
    count1 += 1
print(var_list1)
"""

#print a list containing even numbers in the range 10 - 50
even_nos =[]
for val in range(10,50):
    if val%2 == 0:
        even_nos.append(val)
print(even_nos)

#print a list containing numbers divisible by 2 and not 3 in the range 10 - 50
nos =[]
for val in range(10,50):
    if val%2 == 0 and val%3 != 0: # if val%2 == 0 and not val%3=!= 0:
        nos.append(val)
print(nos)

# while loop
count = 0

while count <= 5:
    print(count)
    count += 1
    print(count)



