"""Нарисовать рамочку шириной w символов и
высотой h символов."""
print("Начало первого задания")


def print_square_1(width, height):
    print("*" * width)
    for i in range(height - 2):
        s = " " * (width - 2)
        print("*" + s + "*")
    print("*" * width)


print_square_1(5, 4)
print("Конец первого задания")

"""Пускай символ, которым рисуется рамочка –
тоже входной параметр."""
print("Начало второго задания")


def print_square_2(width, height, custom_char):
    print(custom_char * width)
    for _ in range(height - 2):
        tmp_str = " " * (width - 2)
        print(custom_char + tmp_str + custom_char)
    print(custom_char * width)


print_square_2(5, 4, "%")
print("Конец второго задания")

"""Нарисовать рамочку шириной w символов и
высотой h символов, и толщиной f символов."""
print("Начало третьего задания")


def print_square_3(width, height, frame):
    for _ in range(frame):
        print("*" * width)
    for _ in range(height - 2):
        tmp_str = " " * (width - frame * 2)
        print("*" * frame + tmp_str + "*" * frame)
    for _ in range(frame):
        print("*" * width)


print_square_3(6, 7, 2)
print("Конец третьего задания")
