"""
Function is a block of coded or statements that perform a certain task and returns a result
"""

def addtwonumbers(x,y): # x,y are parameters, basically variables used in a function
    sum = x + y
    return sum

s1 = addtwonumbers(2,3) # 2,3 are arguments, basically the values used in place of the parameters
#print(s1)

# create a function that prints out the largest number in a list containing a random range of values: basically sort the list in ascending order then print out the largest number
# create a function that takes a list of numbers. Return the largest number
#hackarack....... website for challenges

# A > 79 , B - 60 to 78, C -  59 to 49, D - 48 to 40, E - less 40

# Task 1
def inputselector():
    myinput = input("Please enter a Yes or No: ")
    if myinput == "Yes" or myinput == "yes" or myinput == "YES":
        return "yes"
    elif myinput == "No" or myinput == "no" or myinput == "NO":
        return "No"
    else:
        return "Please ensure your input is a Yes or No"

var_a = inputselector()

print(var_a)


# Task 2
def maxnumber(a, b, c):
    if a > b and a >c:
        val = a
    elif b > a and b > c:
        val = b
    elif c > a and c > b:
        val = c
    else:
        val = "Please check for two or more equal values"
    return val

x = maxnumber(10,10,111)
print(x)

# Task 3
def getfirstandlast(mylist):
    if len(mylist)== 1:
        new_list = [mylist[0]]  # fl = [x[0],x[n-1]]
    else:
        new_list = [mylist[0], mylist[len(mylist) - 1]]# fl = [x[0],x[n-1]]

    return new_list

a = [5, 10, 15, 20, 25]
ret = getfirstandlast(a)
print(ret)

#Task 4
def oddevennumber():

    myno = int(input("Please enter a Number: "))

    if myno > 0:
        if myno%2 == 0 and myno%4 !=0:
            result = "This is an even number"
        elif myno%2 == 0 and myno%4 ==0:
            result = "This is an even number and divisible by 4"
        else:
            result = "This is an odd number"
    else:
        result = "You are trying to divide by zero"

    return result

a = oddevennumber()
print(a)

#task 5
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11)

def splitter(mytup):

    if mytup == tuple:
        ln = int((len(mytup)) / 2)
        part_a = (mytup[(0):ln])  # list = [x[0:(length)/2]]
        part_b = (mytup[ln:])  # list = [x[(length)/2: ]]
        return str(part_a) + '\n' + str(part_b)
    else:
        return "Please ensure you input more than one number"

print(splitter(tup))


###### OR #####

ln = int((len(tup))/2)
part_a = (tup[(0):ln])
part_b = (tup[ln:])

print(part_a)
print(part_b)