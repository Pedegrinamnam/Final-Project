import json

# Спустя столько лет...
def save_game(player):
    data = {
        "money": player.money,
        "rebirths": player.rebirths,
        "upgrades": player.upgrades,
        "total_clicks": player.total_clicks
    }

    with open("save.json", "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_game(player):
    try:
        with open("save.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            player.money = data["money"]
            player.rebirths = data["rebirths"]
            player.upgrades = data["upgrades"]
            player.total_clicks = data["total_clicks"]

    except FileNotFoundError:
        print("Сохранение не найдено. Создаём новую игру.")