print("hello")

number = 3.34


print(number)


i = 23  # int
f = 3.5  # float
s = "hello world"  # str
b = True  # bool
n = None  # NoneType

print(3 + 3)  # 6

print(5 + (6 * 4))  # 29

print(2**2)  # 4

float(23)  # 23.0

int(14.3)  # 14

int(14.99)  # 14 truncates decimal, doesn’t round

round(14.99)  # 15 use this instead


def helloprinter():
    print("hello")


helloprinter()


def multiply(x, y):
    return x*y


value = multiply(2, 3)
print(value)


firstname = "hossein"
lastname = " amiri"
full = firstname + " " + lastname

#name = input("enter your name ")
# print(name)


age = 17
if age > 16:
    print(" you can ")
elif age > 10:
    print("soon")
else:
    print("you cant")


names = ["ali", "hasan", 2]

numbers = set([2, 34, 2, 1, 23, 4, 2, 1])  # avoid dublicate

print(type(names))

print(numbers)


# inventory dictionary
# tuple not change

l = [1,2,3,4] # list

mySet = set([3,4,6]) # set: similar to list but has unique values

myDictionary = {"key": "value"} # dict

myTuple = (3.2,5.6) # tuple




numbers = [34,7,4,24,5]

print(numbers[0]) # 34

numbers[0] = 16

print(numbers[0]) # 16

numbers.append(5) # add 5 to numbers

numbers.pop() # removes last element and returns it

numbers.pop(0) # removes first element and returns it

inventory = {

"iphone X": 16,

"apple airpods": 0,

"ipad pro": 7

}

print(inventory["ipad pro"]) # 7

inventory["ipad pro"] = 6

print(inventory["ipad pro"]) # 6

del inventory["iphone X"]

print(inventory) # {'apple airpods': 0, 'ipad pro': 6}


