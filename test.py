from pyamaze import maze

# функція для вибору алгоритму
def choose_algorithm():
    print("виберіть алгоритм генерації лабіринту:")
    print("1. пріма")
    print("2. рекурсивний пошук з поверненням")
    choice = input("введіть номер алгоритму (1/2): ")
    return choice

# вибір алгоритму
algorithm = choose_algorithm()

# створення лабіринту
m = maze()

# генерація лабіринту залежно від вибраного алгоритму
if algorithm == '1':
    m.CreateMaze(pattern="Prim")  # використовуємо алгоритм пріма
elif algorithm == '2':
    m.CreateMaze(pattern="RecursiveBacktracker")  # використовуємо рекурсивний алгоритм з поверненням
else:
    print("невірний вибір, використовується алгоритм за замовчуванням: пріма.")
    m.CreateMaze(pattern="Prim")

# запуск та відображення лабіринту
m.run()