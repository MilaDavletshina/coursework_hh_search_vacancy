from src.hh_api import HH
from src.vacancies import Vacancy
from src.workfile import JSONSaver
from src.functions import get_greeting


def main():
    """Функция для взаимодействия с пользователем"""

    result = JSONSaver("data/vacancies.json")
    greeting = get_greeting()
    print(greeting)

    keyword = input("Введите вакансию: ")
    api = HH(keyword)
    vacancies_data = api.get_vacancies()
    new_vacancy = [
            Vacancy(data["name"], data.get("salary"), data["url"], data.get("snippet", {}).get("requirement", ""))
            for data in vacancies_data]
    result.add_vacancy(new_vacancy)
    print(f"Найдено {len(new_vacancy)} вакансий.")
    print(f"Данные записаны в файл {result}")
    print()

    top_n = int(input("Введите количество вакансий для сравнения: "))
    new_vacancy = result.save_vacancy()

    if new_vacancy:
        top_vacancies = sorted(new_vacancy, reverse=True)[:top_n]
        for i in top_vacancies:
            print(i.name, i.salary, i.url, i.description)
    print()

    print("Для сортировки по ключевому слову")
    keyword = input("Введите ключевое слово: ")
    new_vacancy = result.save_vacancy()

    filtered_vacancies = [i for i in new_vacancy if i.description and keyword in i.description]
    for i in filtered_vacancies:
        print(i.name, i.salary, i.url, i.description)


if __name__ == "__main__":
    main()