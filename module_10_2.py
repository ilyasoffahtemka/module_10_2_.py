from threading import Thread
from time import sleep

# Общее количество врагов
TOTAL_ENEMIES = 100


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0

    def run(self):
        global TOTAL_ENEMIES
        print(f"{self.name}, на нас напали!")

        while TOTAL_ENEMIES > 0:
            # Уменьшаем количество врагов
            self.days += 1
            remaining_enemies = max(TOTAL_ENEMIES - self.power, 0)
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {remaining_enemies} воинов.")
            TOTAL_ENEMIES = remaining_enemies

            # Ждем 1 секунду, чтобы смоделировать сражение
            sleep(1)

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создаем и запускаем рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

# Дожидаемся окончания всех потоков
first_knight.join()
second_knight.join()

# Вывод сообщения об окончании битв
print("Все битвы закончились!")