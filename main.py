import pygame
import random

from player import Player
from ui.draw import draw_game, draw_shop, draw_rebirth
from sound_manager import SoundManager
from ui.button import Button
from save_manager import save_game, load_game

pygame.init()

screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()

player = Player()

sounds = SoundManager()

load_game(player)

# Музыка, которая делает ♫♫♫♫♫
sounds.play_music(
    "assets/waterfall.mp3"
)

# Рулс Каард который ничего не делает
ralsei_image = pygame.image.load(
    "assets/Lay_Kaard.gif"
)

ralsei_image = pygame.transform.scale(
    ralsei_image,
    (250, 180)
)

# Хамстер, который делает тап-тап
hamster_image = pygame.image.load(
    "assets/ChatGPT_Image_19_июн._2026_г.__20_56_08-removebg-preview.png"
)
hamster_image = pygame.transform.scale(
    hamster_image,
    (250, 200)
)

# Монетки, которые делают динь-динь
coins_image = pygame.image.load(
    "assets/рррр-removebg-preview.png"
)
coins_image = pygame.transform.scale(
    coins_image,
    (35, 35)
)
# Чёрная дыра которая делает оаоаоаОАОАОАОАОАОАОАООАООАОАОАОАОАОАОАОАООААОАОАОАОАОАОАОАОАОАОАООАОАОААААААААААА
black_hole_image = pygame.image.load(
    "assets/black_hole.jpg"
)

black_hole_image = pygame.transform.scale(
    black_hole_image,
    (1400, 1000)
)
#Анимация, которая анимирует
# Кадры анимации Rules Kaard
rules_frames = []

for i in range(63):
    image = pygame.image.load(
        f"assets/Kaards/frame_{i:02d}_delay-0.04s.gif"
    )

    image = pygame.transform.scale(
        image,
        (250, 250)
    )

    # Убираем чёрный фон
    image.set_colorkey((0, 0, 0))

    rules_frames.append(image)

# Текущий кадр анимации
rules_frame = 0
animation_timer = 0
coins = []
rules_timer = 0
shop_open = False
rebirth_open = False

# Сам хомяк (Хомячная кнопка)
click_button = Button(
    500, 250,
    250, 250,
    "HAMSTER"
)
# Сам магазин (Магазинная кнопка)
shop_button = Button(
    1060, 650,
    200, 50,
    "Shop"
)
# Кнопка выхода из магазина (Выходная кнопка)
back_button = Button(
    20, 650,
    200, 50,
    "Back"
)
# Кнопка входа в перерождение ((Почти) перерожденная кнопка)
rebirth_button = Button(
    840, 650,
    200, 50,
    "REBIRTH"
)
# Кнопка выхода из перерождения (Выходно-перерожденная кнопка)
rebirth_back_button = Button(
    20, 650,
    200, 50,
    "BACK"
)
# Кнопка перерождения (Перерожденная кнопка)
rebirth_confirm_button = Button(
    490, 450,
    300, 60,
    "REBIRTH!"
)
# Кнопки всяких улучшалок
house_button = Button(400, 180, 300, 50, "Дом - 10$")
food_button = Button(400, 250, 300, 50, "Хавалка - 500$")
wheel_button = Button(400, 320, 300, 50, "Колесо - 250$")
friend_button = Button(400, 460, 300, 50, "Друг - 5000$")
big_house_button = Button(400, 390, 320, 50, "ДомПобольше - 10000$")

running = True
# Вайл раннинг
while running:
    for event in pygame.event.get():
        # Улучшения в магазе
        if shop_open:
            # Улучшения в магазе
            if shop_open:
                # Дом
                if house_button.clicked(event):
                    player.buy_upgrade("Дом")
                # Хавалка
                if food_button.clicked(event):
                    player.buy_upgrade("Хавалка")
                # Колесо
                if wheel_button.clicked(event):
                    player.buy_upgrade("Колесо")
                # ДомПобольше
                if big_house_button.clicked(event):
                    player.buy_upgrade("ДомПобольше")
                # Друн
                if friend_button.clicked(event):
                    player.buy_upgrade("Друг")
        # Запуск
        if event.type == pygame.QUIT:
            save_game(player)
            running = False
            # Клики
        if not shop_open and click_button.clicked(event):
            player.click()

            for i in range(3):
                coins.append({
                    "x": click_button.rect.centerx,
                    "y": click_button.rect.centery,
                    "vx": random.randint(-6, 6),
                    "vy": random.randint(-14, -8),
                    "life": 80
                })
        # Открыть магаз
        if not shop_open and shop_button.clicked(event):
            shop_open = True
        # Закрыть магаз
        if shop_open and back_button.clicked(event):
            shop_open = False
        # Открыть перерождение
        if not shop_open and not rebirth_open and rebirth_button.clicked(event):
            rebirth_open = True
        # Открыть перерождение
        if not shop_open and not rebirth_open and rebirth_button.clicked(event):
            rebirth_open = True
        # Закрыть перерождение
        if rebirth_open and rebirth_back_button.clicked(event):
            rebirth_open = False
        # Кнопка перерождения
        if rebirth_open and rebirth_confirm_button.clicked(event):
            player.rebirth()

# Иф шоп опен
    if shop_open:
        draw_shop(
            screen,
            player,
            back_button,
            house_button,
            food_button,
            wheel_button,
            friend_button,
            big_house_button,
            rules_frames[rules_frame]
        )
    # Элиф ребиртх опен
    elif rebirth_open:
        draw_rebirth(
            screen,
            player,
            rebirth_back_button,
            rebirth_confirm_button,
            black_hole_image
        )
    # Еслсе драв гейм
    else:
        draw_game(
            screen,
            player,
            click_button,
            shop_button,
            rebirth_button,
            hamster_image,
            coins_image,
            coins
        )
    if shop_open:
        sounds.play_music("assets/M&F.mp3")
    elif rebirth_open:
        sounds.play_music("assets/waterfall.mp3")
    else:
        sounds.play_music("assets/Floppa.mp3")

    for coin in coins:
        # Движение
        coin["x"] += coin["vx"]
        coin["y"] += coin["vy"]
        # Гравитация тянет вниз
        coin["vy"] += 0.5
        # Уменьшаем жизнь
        coin["life"] -= 1

    coins = [
        coin for coin in coins
        if coin["life"] > 0
    ]
    coins = [
        coin for coin in coins
        if coin["y"] > 0
    ]
    rules_timer += 1

    pygame.display.flip()
    rules_timer += 1
    # Обновление анимации Рулса
    if shop_open:
        rules_timer += 1

        if rules_timer >= 10:
            rules_timer = 0
            rules_frame += 1

            if rules_frame >= len(rules_frames):
                rules_frame = 0
    dt = clock.tick(60) / 1000
    player.update(dt)


pygame.quit()