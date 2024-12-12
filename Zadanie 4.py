#3

# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a,b,c):
    area = a * b / 2
    area
    return area

print(f'The area of ​​a triangle with sides 3, 4, 5 is {triangle_area(3, 4, 5)}')
print(f'The area of ​​a triangle with sides 5, 12, 13 is {triangle_area(5, 12, 13)}')
print(f'The area of ​​a triangle with sides 7, 24, 25 is {triangle_area(7, 24, 25)}')

#4

# Calculates the sum of the digits in a number
#
def sum_digits(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')

#5

# Calculates the final grade for a test based
# on the number of points obtained
#Less than 10 points, final grade: Fail
#At least 10 points, final grade: Satisfactory
#At least 14 points, final grade: Good
#At least 18 points, final grade: Excellent

def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points < 18 and points >= 14:
        grade = 'Good'
    elif points < 4 and points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade

test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')

#6

# Function that returns the full name of a day of the week
# based on its number
#
def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'Monday'
    elif day_number == 2:
        result = 'Tuesday'
    elif day_number == 3:
        result = 'Wednesday'
    elif day_number == 4:
        result = 'Thursday'
    elif day_number == 5:
        result = 'Friday'
    elif day_number == 6:
        result = 'Saturday'
    elif day_number == 7:
        result = 'Sunday'
    else:
        result = f'There is no day number {day_number} '
    return result

# Function usage
print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))

#7

###
# Converts letter to corresponding ICAO word
#
def icao(letter):
    letter = letter.capitalize()
    if letter == 'A':
        icao_name = 'Alfa'
    elif letter == 'B':
        icao_name = 'Bravo'
    elif letter == 'C':
        icao_name = 'Charlie'
    elif letter == 'D':
        icao_name = 'Delta'
    elif letter == 'E':
        icao_name = 'Echo'
    elif letter == 'F':
        icao_name = 'Foxtrot'
    elif letter == 'G':
        icao_name = 'Golf'
    elif letter == 'H':
        icao_name = 'Hotel'
    elif letter == 'I':
        icao_name = 'India'
    elif letter == 'J':
        icao_name = 'Juliett'
    elif letter == 'K':
        icao_name = 'Kilo'
    elif letter == 'L':
        icao_name = 'Lima'
    elif letter == 'M':
        icao_name = 'Mike'
    elif letter == 'N':
        icao_name = 'November'
    elif letter == 'O':
        icao_name = 'Oscar'
    elif letter == 'P':
        icao_name = 'Papa'
    elif letter == 'Q':
        icao_name = 'Quebec'
    elif letter == 'R':
        icao_name = 'Romeo'
    elif letter == 'S':
        icao_name = 'Sierra'
    elif letter == 'T':
        icao_name = 'Tango'
    elif letter == 'U':
        icao_name = 'Uniform'
    elif letter == 'V':
        icao_name = 'Victor'
    elif letter == 'W':
        icao_name = 'Whiskey'
    elif letter == 'X':
        icao_name = 'X-ray'
    elif letter == 'Y':
        icao_name = 'Yankee'
    elif letter == 'Z':
        icao_name = 'Zulu'
    else:
        icao_name = '???'

    return icao_name

# Function usage
name = input('Enter your name: ')
print('ICAO words for spelling out your name:')

for char in name:
    word = icao(char)
    print(word, end=" ") 

#8

def time_string(hours, minute, time_format):
    if not 0 <= hours <= 24 or not 0 <= minute <= 59:
        return 'Invalid Time'
    if not time_format in ['12', '24']:
        return 'Invalid Format'
    
    if time_format == '12':
        return f'{hours:02}:{minute:02}'
    else:
        period = 'AM' if hours < 12 else 'PM'
        adjusted_hour = hours % 12 or 12
        return f'{adjusted_hour:02}:{minute:02}{period}'
hours = input('Enter hour: ')
minute = input('Enter minute: ')
time_format = input('Enter time format: ')
time_string(hours, minute, time_format)