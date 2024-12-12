import keyboard

first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter lastname: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n)')

# Prints employee's record
print('DATA RECORD')
print('===========')
print(f'Name: {first_name}', f'{last_name}')
print(f'Age: {age}')
if is_salary_hidden == False:
    print(f'Salary: {salary}')