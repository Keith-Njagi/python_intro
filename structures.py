"""
person = ["John", "Doe", 30 ,65.54, "Mombasa", True]
print(person)
p = person [1:5]
count = 0

#for people in person:
    #print(people)

while count <=5:
    print(person[count])
    count += 1

person_a = ("John", "Doe", 30 ,65.54, "Mombasa", True, "nai")
print(person_a)

w = person
w.clear()
print(w)

po = person.pop(3)
print(po)
"""
#Dictionaries
"""
pers = {
    "firstname":"John",
    "secondname":"Doe",
    "weight":65.54,
    "location":"mombasa",
    "activemember": True
}

print(pers["firstname"],pers["secondname"])
"""

tasklist =[23,"Jane",["Lesson 23",560,{"currency":"KES"}],98701234,(76,"John")]





print(tasklist[2][2]["currency"])
print(tasklist[2][1])
print(len(tasklist))
# change 987 to 789 using an inbuilt function


# tasklist.pop(3)
# print(tasklist.insert(3,789))

no =[0,1,2,3,4,5,6,7,8,9,10]
#list slicing
print((str(tasklist)[::-2]))
print(no[::-2])
print(no[::2])
""" 
using list slicing to print out numbers divisible by 3 in an ordered list
i.e [0,1,2,3,4,5,6,7,8,9,10]
"""
print(no[::3])

# change the name "John" to "Jane"
