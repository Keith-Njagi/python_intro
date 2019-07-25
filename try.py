# task 5
tup = (1)#, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11


def splitter(mytup):

    if mytup == tuple:
        ln = int((len(mytup)) / 2)
        part_a = (mytup[(0):ln])  # list = [x[0:(length)/2]]
        part_b = (mytup[ln:])  # list = [x[(length)/2: ]]
        return str(part_a) + '\n' + str(part_b)
    else:
        return "Please ensure you input more than one number"

print(splitter(tup))
