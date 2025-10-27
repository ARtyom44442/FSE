def draw_rectangle(rows, cols, ch):
    for i in range(rows):
        for j in range(cols):
            print(ch, end="")
        print()

def draw_right_triangle(rows, ch):
    for i in range(1, rows + 1):
        for j in range(i):
            print(ch, end="")
        print()

def draw_frame(rows, cols, ch):
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                print(ch, end="")
            else:
                print(" ", end="")
        print()

n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))
symbol = "#"

print("\nПРЯМОУГОЛЬНИК:")
draw_rectangle(n, m, symbol)

print("\nПРАВЫЙ ТРЕУГОЛЬНИК:")
draw_right_triangle(n, symbol)

print("\nРАМКА:")
draw_frame(n, m, symbol)