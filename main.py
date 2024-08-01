from src.hh_api import HH
from src.vacancies import Vacancy
from src.workfile import JSONSaver
from src.functions import get_greeting


def main():
    """Функция для взаимодействия с пользователем"""

    result = JSONSaver("vacancies.json")
    greeting = get_greeting()
    print(greeting)

    while True:
        print("Выберите пункт меню из предложенных ниже вариантов:")
        print("1. Поиск вакансий")
        print("2. Показать топ N вакансий по зарплате")
        print("3. Найти вакансии по ключевому слову в описании")

        user_choice = input("Выберите пункт меню (1, 2, 3): ")

        if user_choice == '1':

            keyword = input("Введите вакансию: ")
            api = HH(keyword)
            vacancies_data = api.get_vacancies()
            new_vacancy = [Vacancy(data["name"], data.get("salary"), data["url"], data.get("snippet", {}).get("requirement", "")) for data in vacancies_data]
            # result.add_vacancy(new_vacancy)
            print(f"Найдено {len(new_vacancy)} вакансий.")
            break

        elif user_choice == '2':
            top_n = int(input("Введите количество вакансий для сравнения: "))
            new_vacancy = result.get_vacancy()
            if new_vacancy:
                top_vacancies = sorted(new_vacancy, reverse=True)[:top_n]
                for vac in top_vacancies:
                    print(vac.name, vac.salary, vac.url, vac.description)
            else:
                print("Нет вакансий.")
            break

        elif user_choice == '3':
            keyword = input("Введите ключевое слово: ")
            vacancies = result.get_vacancy()
            filtered_vacancies = [vac for vac in vacancies if keyword in vac.description]
            for vac in filtered_vacancies:
                print(vac.name, vac.salary, vac.url, vac.description)
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
        continue


if __name__ == "__main__":
    main()