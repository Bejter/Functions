import draw_figure
print('1. Square')
print('2. Triangle')
print('3. Rectangle')
figure = int(input('Which figure you want to draw?: '))
length = int(input('Enter side A length: '))
if not figure in [1, 2, 3]:
    print('There is no option like this!')
elif figure == 1:
    draw_figure.draw_square(length)
elif figure == 2:
    draw_figure.draw_triangle(length)
else:
    length_b = int(input('Enter side B length: '))
    draw_figure.draw_rectangle(length, length_b)