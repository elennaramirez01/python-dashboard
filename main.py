import datetime

def Sumoftwonum(x, y):
    return x + y
#print(Sumoftwonum(53, 7))

# multiplication is the *, shift + 8
# implementation of multiplication of two numbers goes here:
def multiplicationoftwonum(x, y):
    return x * y
#print(multiplicationoftwonum(5, 10))

# check if sum is valid
# function should accept two numbers and a third number representing the sum
def CheckSumoftwonum(numberOne, numberTwo, expectedSum):
    actualSum = numberOne + numberTwo
    if (actualSum == expectedSum):
        return True
    else:
        return False

#print(CheckSumoftwonum(5, 10, 15))

# check if multiplication of two nums is valid
# function goes here:
def Checkifmultioftwonum(x, y, product):
    if (x * y == product):
        return True
    else:
        return False
#print(Checkifmultioftwonum(3, 5, 15))

### Get the first value in the array
names = ['John', 'Moe', 'Elenna']
#print(names[0])

### get the second value from the names array.
#print(names[1])

## get the last value of the array, use google to determine the python function.
## youu're not supposed to use the index 2. because what if you don't know how many values there are inside any given array

#print(names[-1])

numbersss = [1, 2, 3, 4, 5]
# add each number in the array and return result
def addAll(numArray):
    result = 0
    for num in numArray:
        result = result + num
    return result
# expected is 15
#print(addAll(numbersss))

# multiply each number in the array

def MultiplyAll(numArray):
    result = 1
    for num in numArray:
        result = result * num
    return result
#print(MultiplyAll(numbersss))


# print current date and time in this format Month dd, yyyy HH:MM:SS
#rightNow = datetime.datetime.now()
#print(rightNow.strftime("%B %d, %Y %H:%M:%S"))

# print current date and time in the european/asian format DD/MM/YYYY HH:MM:SS
# use rightnow variable
rightNow = datetime.datetime.now()
#print(rightNow.strftime("%d/%m/%y, %H:%M:%S"))

# Write funtion that lists the contents in an array
Bakery= ["Crossiant", "Donut", "Cookie"]
def PrintArray(StrgArray):
    for Strg in StrgArray:
        print(Strg)
#PrintArray(Bakery)

# Create an array of numbers from a num using python ion range the four
# the input for example could be like 10
# the function should return an array of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def CreateNumsArray(number):
    numbers = []
    for i in range(number):
        numbers.append(i+1)
    return numbers
Hamburger = CreateNumsArray(10)
#print(Hamburger)


def EvenOrOdd(NumArray):
    for Number in NumArray:
        if ((Number % 2) == 0 and (Number % 5) != 0):
            print('The number is even')
        elif (Number % 5) ==0:
            print(f'{Number} is now {Number-0.01}')
        else:
            print('The provided number is odd')
Random = [70,84,5,10]
EvenOrOdd(Random)