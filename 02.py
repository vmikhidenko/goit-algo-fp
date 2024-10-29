import turtle
import math
import time  # для затримки

# Ініціалізація екрану
screen = turtle.Screen()
screen.title("Фрактал 'Дерево Піфагора'")
screen.setup(width=800, height=600)
screen.bgcolor("white")

# Затримка перед створенням черепашки
time.sleep(0.5)

# Налаштування черепашки
t = turtle.Turtle()
t.speed(0)  # максимальна швидкість
t.left(90)  # повертаємо на 90 градусів для вертикального стовбура
t.color("green")

# Функція для створення гілок з рекурсією
def draw_pythagoras_tree(t, length, depth):
    if depth == 0:
        return
    
    # Малюємо стовбур
    t.forward(length)
    
    # Зберігаємо початкове положення і напрямок черепашки
    pos = t.position()
    angle = t.heading()
    
    # Ліва гілка
    t.left(45)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1)
    
    # Повертаємося до початкового положення і кута
    t.setposition(pos)
    t.setheading(angle)
    
    # Права гілка
    t.right(45)
    draw_pythagoras_tree(t, length * math.sqrt(2) / 2, depth - 1)
    
    # Повертаємося назад до основи стовбура
    t.setposition(pos)
    t.setheading(angle)
    t.backward(length)

# Запит у користувача рівня рекурсії
recursion_depth = int(input("Введіть рівень рекурсії: "))

# Позиціюємо черепашку на початкову точку для малювання
t.penup()
t.goto(0, -250)
t.pendown()

# Запускаємо малювання дерева
draw_pythagoras_tree(t, 100, recursion_depth)

# Завершення роботи
screen.mainloop()
