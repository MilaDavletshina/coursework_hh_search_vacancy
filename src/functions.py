import datetime


def get_greeting():
    """Функция приветствия в зависимости от времени суток"""
    now = datetime.datetime.now()
    if 6 <= now.hour < 12:
        return "Доброе утро!"
    elif 12 <= now.hour < 18:
        return "Добрый день!"
    elif 18 <= now.hour < 24:
        return "Добрый вечер!"
    elif 0 <= now.hour < 6:
        return "Доброй ночи!"




if __name__ == "__main__":
    h = get_greeting()
    print(h)
