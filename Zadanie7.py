#3
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
user_input_month = int(input("Enter Month number to see wchich month it is: "))

def writeMonth(user_input_month):
    return months[user_input_month - 1]

print(f"The name of month {user_input_month} is {writeMonth(user_input_month)}")


#4

text = "You never get a second chance to make a first impression"
user_letter = int(input("enter letter to count"))
counter = 0

def calculateLetterInText(text_, letter_):
    for l in text_:
        if l == letter_:
            counter += 1
    return counter

print(f"The number of letter '{user_letter}': {calculateLetterInText(text, user_letter)}")

#5
range_1 = int(input("Enter range min: "))
range_2 = int(input("Enter range max: "))
number_input = int(input("Enter the number: "))

def checkIfWithinRange():
    if(number_input > range_1 and number_input < range_2):
        return True
    return False

print(f"Number {number_input} in the range <{range_1},{range_2}>: {checkIfWithinRange()}")

#6
def hide(card_number):
    card_hidden = " "
    for i, c in enumerate(card_number):
        if i < 2 or i > 12:
            card_hidden += c
        else:
            card_hidden += "*"
    return card_hidden


print(hide("5290312400019022"))
#7

binary = "101101"

def checkIfBinary(binary_number):
    for c in binary_number:
        if c != 1 or c != 0:
            return False
    return True

print(f"{binary} is binary: {checkIfBinary}")

#8

amount = int(input("Enter amount: "))

def coinsCounter(amount_to_pay):
    counter = 0
    while amount_to_pay > 0:
        if amount_to_pay >= 5:
            counter += 1
            amount_to_pay -= 5
        elif amount_to_pay >= 2:
            counter += 1
            amount_to_pay -= 2
        elif amount_to_pay >= 1:
            counter += 1
            amount_to_pay -= 1
    return counter
    
print(f"Amount of coins that must be used: {coinsCounter(amount)}")

#9

number = input("Enter number to count: ")
even_input = input("Sum even or not (y-even, n-odd)")
even = True

if even_input != "y" or even_input != "Y":
    even = False

def sum(number_, even_):
    sum_ = 0
    if even_:
        for c in number_:
            if int(c)%2 == 0:
                sum_ += int(c)
    else:
        for c in number_:
            if int(c)%2 == 1:
                sum_ += int(c)
    return sum_

print(f"{sum(number, even)}")

#10

range_x = int(input("Enter min: "))
range_y = int(input("Enter max: "))

def negEvenSum(x, y):
    sum = 0
    for i in range(x, y):
        if i < 0 and i%2 == 0:
            sum += 1
    return sum

print(f"Negative even numbers in range <{range_x},{range_y}>: {negEvenSum(range_x, range_y)}")

#11

def checkNum(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    return False
    
print(f"is there negative number in numbers: 1, -2, 3: {checkNum(1, -2, 3)}")

#12

number_input = int(input("Enter number: "))

def printAster(n):
    for i in range(n):
        if i == n - 1:
            print("*")
        else:
            print("*/")


printAster(number_input)

#13

def printNumbers(n):
    return ''.join(str(i) for i in range(1, n + 1))

print(printNumbers(11))

#14

def calculator(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        return "Invalid operator"
    
print(f"1 + 2 = {calculator(1, 2, "+")}")

#15

def checkDoors(detector):
    current_people = 0
    for action in detector:
        if action == "+":
            current_people += 1
        elif action == "-":
            current_people -= 1
        if current_people >= 3:
            return True
    return False

print(checkDoors("+-+++-+---"))

#16

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1  
        for _ in range(3, n + 1):
            a, b = b, a + b 
        return b
    
print(fibonacci(10))

#17

def checkIfPal(palindrome):
    return palindrome == palindrome[::-1]

print(checkIfPal("radar"))

#18

def subSpace(sentence):
    return sentence.replace(" ", "")

print(subSpace("A programming language is a system of notation for writing computer programs"))

#19

from collections import Counter

def f(number):
    str_number = str(number)

    digit_count = Counter(str_number)

    total_sum = 0

    for digit, count in digit_count.items():
        if count > 1:
            total_sum += int(digit) * (count - 1)
    
    return total_sum


print(f(513553007))


#20

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def f(n):
    primes = []
    num = 2

    while len(primes) < n:
        if isPrime(num):
            primes.append(num)
        num += 1

    return primes[-1]

#21

def subMaxMin(number1, number2, number3):
    largest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    
    return largest - smallest

print(subMaxMin(12,13,14))

#22

def acronym(name):
    acronym = ''.join(word[0].upper() for word in name.split())
    return acronym

print(acronym("Internet of Things"))

#23

def checkPassword(password):
    if len(password) < 6:
        return False
    
    if len(password) != len(set(password)):
        return False
    
    return True

print("qwerty")

#24

def calcExpression(expression):
    return eval(expression)

print(f("2+3"))

#25

def sumRange(x, y):
    total_sum = 0

    for num in range(x, y + 1):
        if num % 6 == 0 and num % 4 != 0:
            total_sum += num

    return total_sum

print(sumRange(1,20))

#26

def dashText(text):
    if text:
        return '-'.join(text)
    
    return ""

print(dashText("abc"))

#27

def checkingCode(product_code):
    digits = [int(digit) for digit in product_code]
    sum_first_three = sum(digits[:3])
    remainder = sum_first_three % 7
    control_digit = digits[3]

    return remainder == control_digit

print(checkingCode("1114"))

#28
from collections import Counter

def f(dice):
    count = Counter(dice)
    most_common_digit = max(count, key=count.get)
    return int(most_common_digit)

#29

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

#30

def sumNatural(n):
    if n == 1:
        return 1
    else:
        return n + sumNatural(n - 1)
    

result = sumNatural(10)
print(result)

#31
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
