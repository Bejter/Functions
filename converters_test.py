import converter

print('### Test converters')
print(f'Three meters is {converter.m_to_cm(3)}cm')
print(f'150 cm is {converter.cm_to_m(150)}m')
print(f'25 cm is {round(converter.cm_to_in(25))}"')
print(f'5 feet 13 inches is {converter.feet_inches_to_cm(5, 7)}')