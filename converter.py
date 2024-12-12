def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(n):
    return n/2.54

def feet_inches_to_cm(feet, inches):
    return f'{(feet * 12 + inches) * 2.54}cm'

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'150cm = {round(cm_to_in(150), 2)}"')
    print(f'5 feet 13 inches = {str(feet_inches_to_cm(5, 7))}')