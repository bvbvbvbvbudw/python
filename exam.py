import random


def generate_maze(width, height, algorithm="recursive_backtracker"):
    # функція для створення лабіринту, базуючись на обраному алгоритмі
    if algorithm == "recursive_backtracker":
        return generate_with_recursive_backtracker(width, height)  # використовуємо алгоритм "рекурсивний пошук з поверненням"
    elif algorithm == "prim":
        return generate_with_prim(width, height)  # використовуємо алгоритм Пріма
    else:
        raise ValueError(f"Unknown algorithm: {algorithm}")  # помилка, якщо алгоритм невідомий

def generate_with_recursive_backtracker(width, height):
    # генерація лабіринту за допомогою рекурсивного пошуку з поверненням
    maze = [["#" for _ in range(width)] for _ in
            range(height)]  # створюємо двовимірний список, заповнений стінами ('#')
    visited = [[False for _ in range(width)] for _ in
               range(height)]  # створюємо двовимірний список для позначення відвіданих клітинок

    def is_valid(x, y):
        # перевіряємо, чи можна відвідати клітинку (x, y)
        return (1 <= x < height - 1  # координата x повинна бути в межах висоти лабіринту, виключаючи межі
                and 1 <= y < width - 1  # координата y повинна бути в межах ширини лабіринту, виключаючи межі
                and not visited[x][y])  # клітинка не повинна бути вже відвіданою

    def carve_passage(x, y):
        # функція для створення проходів у лабіринті
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]  # можливі напрямки: вправо, вліво, вниз, вгору (через одну клітинку)
        random.shuffle(directions)  # перемішуємо напрямки, щоб вибирати їх у випадковому порядку
        visited[x][y] = True  # позначаємо поточну клітинку як відвідану
        maze[x][y] = " "  # перетворюємо поточну клітинку на прохід (' ')
        for dx, dy in directions:
            nx, ny = x + dx, y + dy  # обчислюємо координати сусідньої клітинки, куди хочемо пройти
            # nx = x + dx (нова координата x), ny = y + dy (нова координата y)
            if is_valid(nx, ny):  # перевіряємо, чи можна потрапити в сусідню клітинку
                maze[x + dx // 2][y + dy // 2] = " "  # створюємо прохід між поточною клітинкою і сусідньою
                # x + dx // 2 - координата стіни по x між поточною і сусідньою клітинками
                # y + dy // 2 - координата стіни по y між поточною і сусідньою клітинками
                carve_passage(nx, ny)  # рекурсивно створюємо проходи з нової клітинки

    carve_passage(1, 1)  # починаємо генерацію з клітинки (1, 1)
    return maze  # повертаємо готовий лабіринт


def generate_with_prim(width, height):
    # генерація лабіринту за допомогою алгоритму Прима
    maze = [["#" for _ in range(width)] for _ in
            range(height)]  # створюємо двовимірний список, заповнений стінами ('#')
    walls = []  # список для зберігання координат стін, які потрібно обробити

    def add_walls(x, y):
        # додаємо сусідні стіни поточної клітинки до списку
        for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:  # напрямки: вправо, вниз, вліво, вгору (через одну клітинку)
            nx, ny = x + dx, y + dy  # обчислюємо координати сусідньої клітинки, до якої прилягає стіна
            # nx = x + dx (нова координата x), ny = y + dy (нова координата y)
            if (0 <= nx < height  # перевіряємо, що координата nx знаходиться в межах висоти лабіринту
                    and 0 <= ny < width  # перевіряємо, що координата ny знаходиться в межах ширини лабіринту
                    and maze[nx][ny] == "#"):  # клітинка повинна бути стіною ('#')
                walls.append((nx, ny, x + dx // 2, y + dy // 2))  # додаємо стіну і координати проходу між клітинками
                # (nx, ny) - координати сусідньої клітинки, (x + dx // 2, y + dy // 2) - координати стіни між клітинками

    maze[1][1] = " "  # початкова точка лабіринту стає проходом (' ')
    add_walls(1, 1)  # додаємо сусідні стіни для початкової точки

    while walls:
        # поки є стіни для обробки
        wx, wy, px, py = walls.pop(random.randint(0, len(walls) - 1))  # вибираємо випадкову стіну зі списку
        # wx, wy - координати стіни, px, py - координати проходу між клітинками
        if maze[wx][wy] == "#":  # перевіряємо, що вибрана стіна ще не оброблена
            maze[wx][wy] = " "  # перетворюємо стіну на прохід (' ')
            maze[px][py] = " "  # перетворюємо міжклітинковий прохід на прохід (' ')
            add_walls(wx, wy)  # додаємо нові стіни, що прилягають до поточної клітинки

    return maze  # повертаємо готовий лабіринт


def display_maze(maze):
    # відображення лабіринту в консоль
    for row in maze:
        print("".join(row))  # об'єднуємо рядок і виводимо


if __name__ == "__main__":
    width, height = 21, 21  # розміри лабіринту
    print("recursive backtracker:")
    rb_maze = generate_maze(width, height, algorithm="recursive_backtracker")
    display_maze(rb_maze)  # відображення лабіринту

    print("prims algorithm:")
    prim_maze = generate_maze(width, height, algorithm="prim")
    display_maze(prim_maze)  # відображення лабіринту